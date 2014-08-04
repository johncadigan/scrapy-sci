from __future__ import print_function
import sys
import string
import re
import shutil
import os
from os.path import join, exists, abspath
from shutil import copytree, ignore_patterns
import ConfigParser

import scrapy
from scrapy.command import ScrapyCommand
from scrapy.utils.template import render_templatefile, string_camelcase
from scrapy.exceptions import UsageError
import scrapy_sci as scrapy_sci

TEMPLATES_PATH = join(scrapy_sci.__path__[0], 'templates')
CLASSIFIERS_PATH = os.getcwd() + os.sep + "data"

TEMPLATES_TO_RENDER = (
    ('${classifier_name}', 'datafeatures.py.tmpl'),
)

IGNORE = ignore_patterns('*.pyc', '.svn')

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return "<classifier>"

    def short_desc(self):
        return "Create new classifier"

    def run(self, args, opts):
        if len(args) != 1:
            raise UsageError()
        classifier_name = args[0]
        if not re.search(r'^[_a-z]*$', classifier_name):
            print('Error: Classifier names must be entirely lower case')
            sys.exit(1)
        elif exists("{0}data{0}{1}".format(os.sep, classifier_name)):
            print("Error: directory %r already exists" % classifier_name)
            sys.exit(1)
        #If this is the first classifier
        if not os.path.exists("data"):
            os.makedirs("data")
            with open("data/__init__.py", "wb") as package_file:
                package_file.close()
        #Make classifier file
        moduletpl = join(TEMPLATES_PATH, 'classifier')
        copytree(moduletpl, join(CLASSIFIERS_PATH, classifier_name), ignore=IGNORE)
        for paths in TEMPLATES_TO_RENDER:
            path = join(*paths)
            tplfile = join(CLASSIFIERS_PATH,
                string.Template(path).substitute(classifier_name=classifier_name))
            render_templatefile(tplfile, classifier_name=classifier_name,
                ClassifierName=string_camelcase(classifier_name))
        #Make settings.cfg file
        config = ConfigParser.RawConfigParser()        
        config.add_section("Classifier")
        classifications = raw_input("Please input classifications separated by commas\n").split(",")
        config.set("Classifier", "classes", ",".join(sorted(c.strip() for c in classifications)))
        for class_type in config.get("Classifier", "classes").split(","):
            keep = int(raw_input("Collect data classified as {0}?\n1. Yes\n 2. No".format(class_type)))
            if keep == 1: 
                config.set("Classifier", class_type, True)
            else:
                config.set("Classifier", class_type, False)
        with open("data/{0}/settings.cfg".format(classifier_name), "wb") as configfile:                
            config.write(configfile)

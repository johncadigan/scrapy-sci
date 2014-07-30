import os
from scrapy.command import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError

from wallpaper.sciscrapy.status import Status
from wallpaper.sciscrapy.classifier import LogisticClassifier, ClassifierCreator

class Command(ScrapyCommand):

    requires_project = True
    
    def syntax(self):
        return "[options] <classifier>"

    def short_desc(self):
        return "Work with a classifier"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-u", "--unreviewed", dest="unreviewed", action="store_true", default=False,
                          help="train and test with unreviewed files")
        parser.add_option("-r", "--reviewed", dest="reviewed", action="store_true", default=True,
                          help="train and test with reviewed files")
        parser.add_option("-t", "--trials", dest="trials", type="int", default=5,
                          help="number of trials to test")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        

    def run(self, args, opts):
        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError("running 'scrapy accuracy' with more than one argument is not supported")
        classifier_name = args[0]
        status = Status()
        CC = ClassifierCreator(status.classifiers[classifier_name])
        if opts.reviewed and opts.unreviewed:
            CC.create_data_set("both")
        elif opts.reviewed:
            CC.create_data_set("reviewed")
        elif opts.unreviewed:
            CC.create_data_set("unreviewed")
        lc = CC.create_classifier(LogisticClassifier)
        lc.estimate_accuracy(opts.trials, verbose=True)
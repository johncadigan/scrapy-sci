# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.contrib.exporter import JsonItemExporter
from scrapy.exceptions import DropItem

from sklearn.linear_model import LogisticRegression

from scrapy_sci.status import Status, Reader
from scrapy_sci.classifier import ClassifierFactory

class ClassifiersPipeline(object):
    
    def __init__(self):
        
        self.status = Status()
        self.classifiers = []
        self.exporters = {}
        for classifier in self.status.classifiers.keys():
            CF = ClassifierFactory(self.status.classifiers[classifier])            
            CF.create_data_set("both")
            lc = lc = CF.create_classifier(LogisticRegression(C=1e5), self.status.classifiers[classifier]['features']())
            lc.fit()
            self.classifiers.append((classifier, lc))
        
        self.classifiers = sorted(self.classifiers, key = lambda a: a[1].estimate_accuracy(5, verbose=True))
        print "Classifier {0} needs the most improvement; selected for export".format(self.classifiers[0][0])
        for classification in self.status.classifiers[self.classifiers[0][0]]['classifications']:
            f = file("{0}.json".format(classification), "wb")
            self.exporters[classification] = JsonItemExporter(f)
                
    
    def process_item(self, item, spider):
        keep = True
        for i, (name, classifier) in enumerate(self.classifiers):
            item_classification = classifier.classify(item)
            if i == 0: export_classification = item_classification
            if self.status.classifiers[name]['classifications'][item_classification] == False:
                raise DropItem("Item removed by classifier: {0}".format(name))
        if keep == True:
            self.exporters[export_classification].export_item(item)

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sciscrapy import status
from sciscrapy.classifier import LogisticClassifier

class ClassifierPipeline(object):
    
    def __init__(self):
        self.status()
        for classification in self.status.classifiers.keys():
            classifications = self.status.classifiers[classifier_name]['classifications']
            classification_possible = True
            data = {c : {} for c in classifications}
            for classification in classifications:
                reviewed = [f for f in self.status.classifiers[classifier_name]['reviewed'] if f.find(classification) >= 0]
                unreviewed = [f for f in self.status.classifiers[classifier_name]['seed'] if f.find(classification) >= 0]
                data[classification]["reviewed"]=reviewed
                data[classification]["unreviewed"]=unreviewed
                if len(reviewed) == 0 and len(unreviewed) == 0: classification_possible = False
                
    
    def process_item(self, item, spider):
        return item

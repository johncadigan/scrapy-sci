# -*- coding: utf-8 -*-

import random
import numpy as np
from sklearn import linear_model

#Labels
from sklearn import preprocessing
#preprocessing.LabelEncoder

#Data

#Testing
from sklearn import cross_validation

from features import FeatureVectorFactory
from status import Reader


class ClassifierWrapper(object):
    
    
    def __init__(self, classifier, X, y, label_encoder, transformer):
        self.classifier = classifier
        self.X = X
        self.y = y
    
    
    def fit(self):
        self.classifier.fit(self.X, self.y)
            
    
    def predict(self, datum):
        guess = self.classifier.predict(transformer.transform(datum))
        return self.label_encoder.inverse_transform(guess[0])
        
    
    def estimate_accuracy(self, trials, verbose=False):
        score = 0.0
        i = 0
        while i < trials:
            X_train, X_test, y_train, y_test = cross_validation.train_test_split(
            self.X, self.y, test_size=0.4, random_state=0)
            self.classifier.fit(X_train, y_train)
            score +=self.classifier.score(X_test,y_test)
            i+=1
        if verbose: print "Average accuracy over {0} iterations: {1} ".format(trials, score/float(i))
        return score / float(i)
    

class ClassifierFactory(object):
    
    def __init__(self, classifier_dic):
        self.classifier = classifier_dic
        classifications = self.classifier['classifications']
        self.possible = True
        self.unreviewed = True
        self.reviewed = True
        self.data_files = {c : {} for c in classifications}
        for classification in classifications:
            seed = [f for f in self.classifier['seed'] if f.find(classification) >= 0]
            reviewed = [f for f in self.classifier['reviewed'] if f.find(classification) >= 0]
            unreviewed = [f for f in self.classifier['unreviewed'] if f.find(classification) >= 0]
            self.data_files[classification]["seed"]=seed
            self.data_files[classification]["reviewed"]=reviewed                
            self.data_files[classification]["unreviewed"]=unreviewed
            if len(reviewed) == 0 and len(seed) == 0:
                self.reviewed = False
            if len(unreviewed) == 0:
                self.unreviewed = False
            if self.unreviewed == False and self.reviewed == False:
                self.possible = False
        self.data = [] #Data features
        self.labels = [] #Data labels
                
    def create_data_set(self, data_type):
        for classification in self.data_files.keys():
            if data_type == "reviewed" or data_type == "both":
                for f in self.data_files[classification]["reviewed"]:
                    datum =Reader.read_reviewed(f)
                    if datum:
                        self.data.append(datum)
                        self.labels.append(classification)
                if data_type == "both":
                    for fs in self.data_files[classification]["seed"]:
                        for datum in Reader.read_seed(fs):
                            self.data.append(datum)
                            self.labels.append(classification)
            if data_type == "unreviewed" or data_type == "both":
                 for f in self.data_files[classification]["unreviewed"]:
                    for datum in Reader.read_seed(fs):
                        self.data.append(datum)
                        self.labels.append(classification)
    
    def test_classifier(self, scikit_classifier, transformer, trials):
        X = transformer.fit_transform(self.data)
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(self.labels)
        cw = ClassifierWrapper(scikt_classifier, X, y, transformer, le)
        return cw.estimate_accuracy(trials, verbose = True)
        
        
    def fit_classifier(self, scikit_classifier, transformer):
        X = transformer.fit_transform(self.data)
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(self.labels)
        cw = ClassifierWrapper(scikt_classifier, X, y, transformer, le)
        return cw.fit()
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

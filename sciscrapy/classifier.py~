# -*- coding: utf-8 -*-

import random
import numpy as np
from sklearn import linear_model
from features import FeatureVectorFactory

from status import Reader


class LogisticClassifier(object):
    
    
    def __init__(self, feature_extractor, data, labels, h=.02, c=1e5):
        self.FVF = FeatureVectorFactory(feature_extractor, [item for item,label in data])
        self.data = data
        random.shuffle(self.data)
        self.i_labels = {}
        self.o_labels = {}
        for i, label in enumerate(sorted(labels)):
            self.i_labels[label] = i #internal labels
            self.o_labels[i] = label # external labels
        self.classifier = linear_model.LogisticRegression(C=c)
    
    
    def train(self):
        X = []
        Y = []
        for datum in self.data:
            x,y = datum
            X.append(self.FVF.make_vector(x))
            Y.append(self.i_labels[y])
        X = np.array(X)
        Y = np.array(Y)
        self.classifier.fit(X,Y)
            
    
    def classify(self, datum):
        guess = self.classifier.predict(self.FVF.make_vector(datum))
        return self.o_labels[guess[0]]
        
    
    def estimate_accuracy(self, iterations, verbose=False):
        score = 0.0
        i = 0
        while i < iterations:
            random.shuffle(self.data)
            train, test = self.data[:len(self.data)/2], self.data[len(self.data)/2:]
            #Train        
            X = []
            Y = []
            for datum in train:
                x,y = datum
                X.append(self.FVF.make_vector(x))
                Y.append(self.i_labels[y])
            X = np.array(X)
            Y = np.array(Y)
            self.classifier.fit(X,Y)
            #Test
            M = []
            N = []
            for datum in test:
                x,y = datum
                M.append(self.FVF.make_vector(x))
                N.append(self.i_labels[y])
            M = np.array(M)
            N = np.array(N)
            i += 1
            score +=self.classifier.score(M,N)
        if verbose: print "Average accuracy over {0} iterations: {1} ".format(iterations, score/float(i))
        return score / float(i)
    

class ClassifierCreator(object):
    
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
                
    def create_data_set(self, data_type):
        self.data = [] #For tuples of (dic, classification) to be passed to classifier
        for classification in self.data_files.keys():
            if data_type == "reviewed" or data_type == "both":
                for f in self.data_files[classification]["reviewed"]:
                    datum =Reader.read_reviewed(f)
                    if datum:
                        self.data.append((datum, classification))
                if data_type == "both":
                    for fs in self.data_files[classification]["seed"]:
                        for datum in Reader.read_seed(fs):
                            self.data.append((datum, classification))
            if data_type == "unreviewed" or data_type == "both":
                 for f in self.data_files[classification]["unreviewed"]:
                    for datum in Reader.read_seed(fs):
                        self.data.append((datum, classification))
        
    def create_classifier(self, classifier_type):
        c = classifier_type(self.classifier['features'], self.data, sorted(self.classifier['classifications']))
        return c
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

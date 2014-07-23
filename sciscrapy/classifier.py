# -*- coding: utf-8 -*-

import random
import numpy as np
from sklearn import linear_model
from features import FeatureVectorFactory



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
            
    
    def classify(datum):
        guess = self.classifier.predict(self.FVF.make_vector(datum))
        return self.o_labels[guess]
        
    
    def estimate_accuracy(self, iterations):
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
        return score / float(i)
        
        

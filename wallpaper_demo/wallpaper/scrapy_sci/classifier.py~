# -*- coding: utf-8 -*-
from __future__ import print_function
from time import time

import numpy as np
np.set_printoptions(threshold=np.nan)
np.set_printoptions(linewidth=150)

from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, chi2

from status import Reader


class ClassifierWrapper(object):
    
    
    def __init__(self, classifier, X, y, label_encoder, transformer):
        self.classifier = classifier
        self.label_encoder = label_encoder
        self.transformer = transformer
        self.X = X
        self.y = y
    
    #Implementation of standard classifier functions
    def fit(self,X=None, y=None):
        if X == None and y == None:
            self.classifier.fit(self.X, self.y)
        else:
            self.classifier.fit(X,y)
            
    def predict(self, data_features):
        return self.classifier.predict(data_features)
    
    
    #Other functions
    def classify(self, datum):
        guess = self.classifier.predict(self.transformer.transform(datum))
        return self.label_encoder.inverse_transform(guess[0])
    
    def benchmark(self, top_n=0, confusion_matrix=False, report=False, verbose=False):
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(
            self.X, self.y, test_size=0.4, random_state=0)
        #feature_names = np.asarray(self.transformer.get_feature_names())
        categories = list(self.label_encoder.classes_)
        if verbose:
            print('_' * 80)
            print("Training: ")
            print(self.classifier)
        t0 = time()
        self.classifier.fit(X_train, y_train)
        train_time = time() - t0
        if verbose: print("train time: {:.3}s".format(train_time))

        t0 = time()
        pred = self.classifier.predict(X_test)
        test_time = time() - t0
        if verbose: print("test time: {:.3}s".format(train_time))

        score = metrics.f1_score(y_test, pred)
        if verbose: print("f1 score: {:.3}".format(score))

        if hasattr(self.classifier, 'coef_') and verbose and False:#No feature names yet
            print("dimensionality: %d" % self.classifier.coef_.shape[1])
            print("density: %f" % density(clf.coef_))
            if top_n > 0 and feature_names is not None:
                print("top {0} keywords per class:".format(top_n))
                for i, category in enumerate(categories):
                    topn = np.argsort(clf.coef_[i])[-top_n:]
                    print("{0}: {1}".format(category, " ".join(feature_names[topn])))
            print()

        if report:
            print("classification report:")
            print(metrics.classification_report(y_test, pred,
                                                target_names=categories))

        if confusion_matrix:
            print("confusion matrix:")
            print(["{0}:{1}".format(i, category) for (i, category) in enumerate(categories)])
            print(metrics.confusion_matrix(y_test, pred))

        if verbose: print()
        clf_descr = str(self.classifier).split('(')[0]
        return clf_descr, score, train_time, test_time #For comparative printout

    def estimate_accuracy(self, trials, verbose=False):
        score = 0.0
        i = 0
        while i < trials:
            X_train, X_test, y_train, y_test = cross_validation.train_test_split(
            self.X, self.y, test_size=0.4, random_state=0)
            self.classifier.fit(X_train, y_train)
            score +=self.classifier.score(X_test,y_test)
            i+=1
        if verbose: print("Average accuracy over {0} iterations: {1} ".format(trials, score/float(i)))
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
            seed = [f for f in self.classifier['seed'] if f.find(classification) == 0]
            reviewed = [f for f in self.classifier['reviewed'] if f.find(classification) == 0]
            unreviewed = [f for f in self.classifier['unreviewed'] if f.find(classification) == 0]
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
        
        
    def create_classifier(self, scikit_classifier, transformer):
        t = transformer
        X = t.fit_transform(self.data)
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(self.labels)
        cw = ClassifierWrapper(scikit_classifier, X, y, le, t)
        return cw
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

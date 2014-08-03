import os
import sys
from time import time

import matplotlib.pyplot as plt

import numpy as np
from scrapy.command import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError

from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB


from scrapy_sci.status import Status
from scrapy_sci.classifier import ClassifierFactory

class Command(ScrapyCommand):

    requires_project = True
    
    def syntax(self):
        return "[options] <classifier>"

    def short_desc(self):
        return "Estimate the accuracy of a classifier"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-u", "--unreviewed", dest="unreviewed", action="store_true", default=False,
                          help="train and test with unreviewed files")
        parser.add_option("-r", "--reviewed", dest="reviewed", action="store_true", default=True,
                          help="train and test with reviewed files")
                        
        parser.add_option("--report", action="store_true", dest="print_report", default=False,
                          help="Print a detailed classification report.")
        parser.add_option("--confusion_matrix", action="store_true", dest="print_cm", default=False,
                      help="Print the confusion matrix.")
        #Not supported:
        parser.add_option("-t", "--top-n-features", dest="topn", type="int", default=0,
                          help="number of top features to reveal")

    def run(self, args, opts):
        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError("running 'scrapy benchmark' with more than one argument is not supported")
        classifier_name = args[0]
        status = Status()
        CF = ClassifierFactory(status.classifiers[classifier_name])
        if opts.reviewed and opts.unreviewed:
            CF.create_data_set("both")
        elif opts.reviewed:
            CF.create_data_set("reviewed")
        elif opts.unreviewed:
            CF.create_data_set("unreviewed")
        results = []
        lc = CF.create_classifier(LogisticRegression(C=1e5), status.classifiers[classifier_name]['features']())
        results.append(lc.benchmark(opts.topn, opts.print_cm, opts.print_report, verbose=True))
        
##        for clf, name in (
##            (RidgeClassifier(tol=1e-2, solver="lsqr"), "Ridge Classifier"),
##            (Perceptron(n_iter=50), "Perceptron"),
##            (PassiveAggressiveClassifier(n_iter=50), "Passive-Aggressive")
##            ):
##            print('=' * 80)
##            print(name)
##            c = CF.create_classifier(clf, status.classifiers[classifier_name]['features']())
##            results.append(c.benchmark(opts.topn, opts.print_cm, opts.print_report, verbose=True))        
        
        indices = np.arange(len(results))

        results = [[x[i] for x in results] for i in range(4)]
        clf_names, score, training_time, test_time = results
        training_time = np.array(training_time) / np.max(training_time)
        test_time = np.array(test_time) / np.max(test_time)
        plt.figure(figsize=(12, 8))
        plt.title("Score")
        plt.barh(indices, score, .2, label="score", color='r')
        plt.barh(indices + .3, training_time, .2, label="training time", color='g')
        plt.barh(indices + .6, test_time, .2, label="test time", color='b')
        plt.yticks(())
        plt.legend(loc='best')
        plt.subplots_adjust(left=.25)
        plt.subplots_adjust(top=.95)
        plt.subplots_adjust(bottom=.05)

        for i, c in zip(indices, clf_names):
            plt.text(-.3, i, c)
        plt.show()
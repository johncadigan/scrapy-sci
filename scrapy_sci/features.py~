# -*- coding: utf-8 -*-

import inspect
import numpy as np
from sklearn.feature_extraction import DictVectorizer


class DictVectWrapper(object):
    
    def __init__(self):
        self.feature_extractors = [extractor[1] for extractor in inspect.getmembers(self, predicate=inspect.ismethod) if extractor[0].find("feature") > 0]
        self.dv = DictVectorizer()
        
    def fit(self, data):
        data_dics = []
        for datum in data:
            features = {}
            for feature in self.feature_extractors:
                features.update(feature(datum))
            data_dics.append(features)
        self.dv.fit(data_dics)
    
    def fit_transform(self, data):
        data_dics = []
        for datum in data:
            features = {}
            for feature in self.feature_extractors:
                features.update(feature(datum))
            data_dics.append(features)
        res = self.dv.fit_transform(data_dics)
        return res
    
    def transform(self, datum):
        features = {}
        for feature in self.feature_extractors:
            features.update(feature(datum))
        return self.dv.transform(features)
    
##    def get_feature_names(self):
##        return self.dv.get_feature_names() 
    
    
    
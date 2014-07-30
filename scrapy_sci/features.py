# -*- coding: utf-8 -*-

import inspect
import numpy as np



class FeatureVectorFactory(object):
    
    def __init__(self, FeatExtractor, data):
        self.FE = FeatExtractor()
        self.aligned_features = {}
        for datum in data:
            self.aligned_features.update(self.FE.extract(datum))
        self.aligned_features = {key : 0.0 for key in self.aligned_features.keys()}
    
    def make_vector(self, datum):
        fv = dict(self.aligned_features)
        fv.update(self.FE.extract(datum))
        return np.array([fv[k] for k in self.aligned_features.keys()])
    
    

class FeatureExtractor(object):
    
    def __init__(self):
        self.feature_extractors = [extractor[1] for extractor in inspect.getmembers(self, predicate=inspect.ismethod) if extractor[0].find("feature") > 0]
    
    def extract(self, datum):
        features = {}
        for feature in self.feature_extractors:
            features.update(feature(datum))
        return features
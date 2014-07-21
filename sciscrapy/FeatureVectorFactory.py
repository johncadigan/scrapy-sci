import numpy as np

class FeatureVectorFactory(object):
    
    def __init__(self, FeatureExtractor, data):
        self.FE = FE()
        self.aligned_features = {}
        for datum in data:
            self.aligned_features.update(FE.extract(datum))
        self.aligned_features = {key : 0.0 for key in self.aligned_features.keys()}
    
    def make_feature_vector(self, datum):
        fv = dict(self.aligned_features)
        fv.update(self.FE.extract(features))
        return np.array([fv[k] for k in self.aligned_features.keys()])
    

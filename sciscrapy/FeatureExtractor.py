import inspect

class FeatureExtractor(object):
    
    def __init__(self):
        self.feature_extractors = [extractor[1] for extractor in inspect.getmembers(self, predicate=inspect.ismethod) if extractor[0].find("feature") > 0]
    
    def extract(self, datum):
        features = {}
        for feature in self.feature_extractors:
            features.update(feature(datum))
        return features
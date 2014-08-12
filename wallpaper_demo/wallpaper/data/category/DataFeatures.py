# -*- coding: utf-8 -*-


from scrapy_sci.features import DictVectWrapper

class DataFeatures(DictVectWrapper):
    
    def __init__(self):
        super(DataFeatures, self).__init__()
    
    def dimension_features(self, datum):
        features = {}
        x = float(datum["x_resolution"])
        y = float(datum["y_resolution"])
        if x / y > 3: features['wide'] = 1.0
        return features

    def color_features(self, datum):
        features = {}
        for color in datum['colors']:
            features['color({0})'.format(color.encode('utf-8'))] = 1.0
        #features["n_colors"] = float(len(datum['colors']))
        return features
    
    def descriptor_features(self, datum):
        features = {'named' : 0.0}
        for descriptor in datum['descriptors']:
            features["tag({0})".format(descriptor.encode('utf-8'))] = 1.0
            if descriptor.encode('utf-8')[0].isupper(): features['named'] = 1.0
        #features["n_tags"] = float(len(datum['descriptors']))
        return features 
    
    
    

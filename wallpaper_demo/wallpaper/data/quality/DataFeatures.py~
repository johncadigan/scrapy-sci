from sciscrapy.features import FeatureExtractor

class DataFeatures(FeatureExtractor):
    
    def __init__(self):
        super(DataFeatures, self).__init__()
    
    
    def dimension_features(self, datum):
        x = float(datum["x_resolution"])
        y = float(datum["y_resolution"])
        features = {"x_dim" : x, "y_dim": y, "combined": x*y}
        return features
    
    def viewer_features(self, datum):
        features = {'views' : float(datum['views']), "favorites" : float(datum['favorites'])}
        return features
    
    



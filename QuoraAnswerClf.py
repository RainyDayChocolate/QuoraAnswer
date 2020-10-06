import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import
class AnswerClassifier:

    def __init__(self):

        self._model = None
        self.useful_features = [str(i) for i in range(1, 22)]

    def preprocess_feature(self, features_strings):
        features = []
        for feature in features_strings:
            _id, val = feature.split(':')
            _id, val = eval(_id), eval(val)
            if _id < 23:
                features.append(val)
        return features

    def preprocess_train_data(self, record):
        record = record.split(' ')
        y = eval(record[1])
        y = y > 0
        for 



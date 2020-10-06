import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import
class AnswerClassifier:

    def __init__(self):

        self._model = None
        self.useful_features = set([i for i in range(1, 22)])
        self.useful_features.remove(19)
        self.pre_processer = sklearn.
    def preprocess_feature(self, features_string):
        features = []
        for feature in features_string:
            _id, val = feature.split(':')
            _id, val = eval(_id), eval(val)
            if _id < 23:
                if _id == 1:
                    val = val ** (1 / 4)
                if _id == 12:
                    val = val if val < 10 else 10
                if _id == 20:
                    val = val if val < 20 else 20
                features.append(val)
        return features

    def preprocess_train_data(self, record):
        record = record.split(' ')
        y = eval(record[1])
        y = y > 0
        X = self.preprocess_feature(record[2:])
        return X, y

    def preprocess_test_data(self, record):
        record = record.split(' ')
        X = self.preprocess_feature(record[1:])






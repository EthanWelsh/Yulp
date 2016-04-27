from abc import abstractmethod, ABCMeta

import numpy as np


class FeatureVector:

    def __init__(self):
        self.features = []

    def append(self, feature):
        if not isinstance(feature, Feature):
            raise TypeError

        self.features.append(feature)

    def train(self, reviews, labels):
        for feature in self.features:
            feature.train(reviews, labels)

    def score(self, review):
        return [feature.score(review) for feature in self.features]


class Feature:
    __metaclass__ = ABCMeta

    @abstractmethod
    def train(self, reviews, labels):
        """
        Do whatever preparations which are needed to train your feature

        """
        pass

    @abstractmethod
    def score(self, data):
        """
        Provides some scalar value as representation of this feature's score

        :param data: a single review or list of reviews to score
        """
        pass

    def save(self, path):
        """
        Saves pre-trained object to the given path.

        :param path: the path to save the data to
        """
        pass

    def load(self, path):
        """
        Retrieve pre-trained object from the given path.

        :param path: the path to load the data from
        """
        pass

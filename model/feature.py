import abc
import os


class FeatureVector:

    def __init__(self):
        self.features = []

    def append(self, feature):
        self.features.append(feature)

    def train(self, data, labels):
        for feature in self.features:
            feature.train(data, labels)

    def score(self, data):
        return [[feature.score(datum) for feature in self.features] for datum in data]


class Feature:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def train(self, data, labels):
        """
        :param data: A list of tuples containing training data and associated tag.
        :param labels: A parallel array of matching labels for each piece of training data
        """
        return

    @abc.abstractmethod
    def score(self, data):
        """
        Provides some scalar value as representation of this feature's score
        :param data: a single review or list of reviews to score
        """
        return

    @abc.abstractmethod
    def save(self, path):
        """Save's pre-trained object to the given path."""

    @abc.abstractmethod
    def load(self, path):
        """Retrieve pre-trained object from the given path."""
        return

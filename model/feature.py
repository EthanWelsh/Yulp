from abc import abstractmethod, ABCMeta


class FeatureVector:

    def __init__(self):
        self.features = []

    def append(self, feature):
        if not isinstance(feature, Feature):
            raise TypeError

        self.features.append(feature)

    def train(self):
        for feature in self.features:
            feature.train()

    def score(self, data):
        return [[feature.score(datum) for feature in self.features] for datum in data]


class Feature:
    __metaclass__ = ABCMeta

    @abstractmethod
    def train(self):
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

    @abstractmethod
    def save(self, path):
        """
        Saves pre-trained object to the given path.

        :param path: the path to save the data to
        """
        pass

    @abstractmethod
    def load(self, path):
        """
        Retrieve pre-trained object from the given path.

        :param path: the path to load the data from
        """
        pass

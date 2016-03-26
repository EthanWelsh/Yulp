import abc


class Feature:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def train(self, data):
        """
        :param data: A list of tuples containing training data and associated tag.
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

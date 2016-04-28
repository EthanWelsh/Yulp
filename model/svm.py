import numpy as np
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier


class SVM:
    def __init__(self, feature_vector):
        self.features = feature_vector
        self.clf = OneVsRestClassifier(svm.SVC(kernel='rbf'))

    def train(self, reviews, labels):
        if len(reviews) != len(labels):
            raise TypeError

        review_scores = [self.features.score(review) for review in reviews]
        self.clf.fit(review_scores, labels)

    def predict(self, data):
        dec = self.clf.predict(np.array([self.features.score(data)]))
        return dec[0]

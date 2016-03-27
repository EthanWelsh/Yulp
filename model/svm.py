from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier


class SVM:
    def __init__(self, feature_vector):
        self.features = feature_vector
        self.clf = OneVsRestClassifier(svm.SVC())

    def train(self, data, labels):
        self.clf.fit(self.features.score(data), labels)

    def predict(self, data):
        dec = self.clf.decision_function(self.features.score(data))
        return dec.shape[1]

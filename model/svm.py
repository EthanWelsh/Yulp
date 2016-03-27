from sklearn import svm


class SVM:
    def __init__(self, feature_vector):
        self.features = feature_vector
        self.clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=None, degree=3,
                           gamma='auto', kernel='rbf', max_iter=-1, probability=False, random_state=None,
                           shrinking=True, tol=0.001, verbose=False)

    def train(self, data, labels):
        self.clf.fit(self.features.score(data), labels)

    def predict(self, data):
        self.clf.predict(self.features.score(data))


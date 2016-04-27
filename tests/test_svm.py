from itertools import chain

import numpy as np
import pytest
from model.feature import Feature, FeatureVector
from model.svm import SVM


class TestSVM:

    sample_reviews = ['I HATE this place a lot'.split(),
                      'it was pretty good.'.split(),
                      'All in all not too bad!'.split(),
                      'Great for the price!'.split()]

    sample_labels = np.array([1, 1, 0, 0]).reshape(-1, 1)


    class BogusFeature(Feature):
        def load(self, path):
            pass

        def train(self):
            pass

        def score(self, data):
            data = ' '.join(list(chain.from_iterable(data)))

            return 1 if data.islower() else 0,

        def save(self, path):
            pass

    def test_train(self):

        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        try:
            SVM(feature_vector=fv).train(reviews=TestSVM.sample_reviews, labels=TestSVM.sample_labels)
        except:
            pytest.fail('SVM training failed')

    def test_train_improper_arguments(self):
        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        with pytest.raises(TypeError):
            SVM(feature_vector=fv).train(reviews=TestSVM.sample_reviews, labels=TestSVM.sample_labels[:-1, :])

    def test_svm_predict(self):

        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        svm = SVM(feature_vector=fv)
        svm.train(reviews=TestSVM.sample_reviews, labels=TestSVM.sample_labels)

        assert svm.predict(['HI']) == 0 or svm.predict(['HI']) == 1
        assert svm.predict(['earth']) == 0 or svm.predict(['earth']) == 1






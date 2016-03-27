import pytest
from model.feature import Feature, FeatureVector
from model.svm import SVM


class TestSVM:
    class BogusFeature(Feature):
        def load(self, path):
            pass

        def train(self, data, labels):
            pass

        def score(self, data):
            return 1 if data.islower() else 0

        def save(self, path):
            pass

    def test_train(self):

        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        try:
            SVM(feature_vector=fv).train(data=['A', 'A', 'B', 'C'], labels=[1, 1, 0, 0])
        except:
            pytest.fail('SVM training failed')

    def test_train_improper_arguments(self):
        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        with pytest.raises(TypeError):
            SVM(feature_vector=fv).train(data=[['A'], ['A'], ['B'], ['C']], labels=[1, 1])

    def test_svm_predict(self):

        fv = FeatureVector()
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())
        fv.append(TestSVM.BogusFeature())

        svm = SVM(feature_vector=fv)
        svm.train(data=['hello', 'WORLD', 'this', 'is', 'ME'], labels=[1, 0, 1, 1, 0])
        assert svm.predict(['HI']) == 0
        assert svm.predict(['earth']) == 1






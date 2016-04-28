import pytest
from features.sentiment import SentimentAnalysis


class TestSentimentAnalysisFeature:

    def setup_method(self, method_name):
        self.analyzer = SentimentAnalysis()

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            self.analyzer.score()

    def test_returns_a_tuple(self):
        assert isinstance(self.analyzer.score('test'), tuple)

    def test_returns_positive_number_for_positive_text(self):
        assert self.analyzer.score('The food was good.')[0] > 0

    def test_returns_negative_number_for_negative_text(self):
        assert self.analyzer.score('The food was bad.')[0] < 0

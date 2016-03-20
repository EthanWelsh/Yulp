import pytest
from sentiment_analysis import sentiment_analysis


class TestSentimentAnalysisFeature:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            sentiment_analysis()

    def test_returns_a_number(self):
        assert isinstance(sentiment_analysis('test'), float)

    def test_returns_positive_number_for_positive_text(self):
        assert sentiment_analysis('The food was good.') > 0

    def test_returns_negative_number_for_negative_text(self):
        assert sentiment_analysis('The food was bad.') < 0

import pytest
from features.average_word_length import AverageWordLength


class TestAverageWordLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            AverageWordLength().score()

    def test_returns_a_tuple(self):
        assert isinstance(AverageWordLength().score([['test']]), tuple)

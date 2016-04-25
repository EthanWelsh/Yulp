import pytest
from features.spelling_analysis import Spelling


class TestAverageWordLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            Spelling().score()

    def test_returns_a_number(self):
        assert isinstance(Spelling().score([['test']]), float)
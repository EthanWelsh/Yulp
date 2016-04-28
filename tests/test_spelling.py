import pytest
from features.spelling import Spelling


class TestAverageWordLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            Spelling().score()

    def test_returns_a_tuple(self):
        assert isinstance(Spelling().score([['test']]), tuple)
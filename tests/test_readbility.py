import pytest
from features.readability import Readability


class Test_Readability:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            Readability().score()

    def test_returns_a_number(self):
        assert isinstance(Readability().score([['test']]), tuple)
        assert isinstance(Readability().score([['test']])[0], float)
        assert isinstance(Readability().score([['test']])[1], float)
        assert isinstance(Readability().score([['test']])[2], float)
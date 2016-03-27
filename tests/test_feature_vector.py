import pytest


class TestFeature:
    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            AverageWordLength().score()

    def test_returns_a_number(self):
        assert isinstance(AverageWordLength().score([['test']]), float)
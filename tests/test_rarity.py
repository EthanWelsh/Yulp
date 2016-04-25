import pytest
from features.rarity_analysis import Rarity


class TestAverageWordLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            Rarity().score()

    def test_returns_a_number(self):
        assert isinstance(Rarity().score([['test']]), float)
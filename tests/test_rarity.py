import pytest
from features.rarity import Rarity


class TestAverageWordLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            Rarity().score()

    def test_returns_a_tuple(self):
        assert isinstance(Rarity().score([['test']]), tuple)

import pytest
from features.average_sent_length import AverageSentLength


class TestAverageSentLength:

    def test_it_fails_without_passing_text(self):
        with pytest.raises(TypeError):
            AverageSentLength().score()

    def test_returns_a_number(self):
        assert isinstance(AverageSentLength().score([['test']]), float)

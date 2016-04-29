from features.sentence_topic import SentenceTopic


class SentenceTopicTestClass(SentenceTopic):

    def _get_food_types(self):
        s = set()
        s.add('foo')
        s.add('bar')
        s.add('foo bar')
        return s


class TestSentenceTopicFeature:

    def test_it_removes_multi_word_food_items(self):
        feature = SentenceTopicTestClass()
        assert len(feature.food_words) == 2

    def test_it_detects_sentences_with_food_words(self):
        feature = SentenceTopicTestClass()
        assert feature._sentence_contains_food_word(['foo']) is True
        assert feature._sentence_contains_food_word(['Foo']) is True
        assert feature._sentence_contains_food_word(['bar']) is True
        assert feature._sentence_contains_food_word(['baz']) is not True
        assert feature._sentence_contains_food_word(['baz', 'foo']) is True

    def test_it_scores_reviews(self):
        feature = SentenceTopicTestClass()
        assert feature.score([
            ['foo'], ['bar']
        ]) == 1
        assert feature.score([
            ['foo'], ['baz']
        ]) == .5

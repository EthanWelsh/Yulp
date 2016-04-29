from model.feature import Feature
from functools import reduce


class SentenceTopic(Feature):

    def __init__(self):
        words = self._get_food_types()
        words = filter(lambda entry: len(entry.split(' ')) == 1, words)
        self.food_words = set(words)

    def score(self, data):
        """
        Score a review

        *Must* take an array of sentences

        Returns:
            float: percentage of sentences about food
        """
        total_sentences = len(data)

        def num_food_sentences(prev, sentence):
            if self._sentence_contains_food_word(sentence):
                return prev + 1
            else:
                return prev

        food_sentences = reduce(num_food_sentences, data, 0)
        return (food_sentences / total_sentences, )

    def _sentence_contains_food_word(self, sentence):
        """
        Get whether or not a sentence is about food

        Returns:
            boolean: whether or not it's about food
        """
        sentence = list(map(lambda word: word.lower(), sentence))
        return reduce(lambda prev, word: prev or (word in self.food_words),
                      sentence,
                      False)

    def _get_food_types(self, food_words_path='data/food_words.txt'):
        """
        Get the list of food types

        Only includes lines from the dictionary that contain a single word

        Returns:
            set(<str>): the set of words
        """
        words = set()
        with open(food_words_path, encoding='utf-8') as f:
            for line in f.readlines():
                if len(line.split(' ')) == 1:
                    words.add(line)
        return words

import re, collections
from model.feature import Feature
import string

"""
dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010.
<http://wordnet.princeton.edu>
"""


class Spelling(Feature):
    def __init__(self):
        self.word_counts = {}

    def spelling_analysis(self, text):
        """
        :return: value between 0 and 1 representing the proportion of correctness where 1 is everything spelled
        correctly, 0 is everything spelled incorrectly
        """

        misspellings = 0
        total_words = 0

        for sentence in text:
            total_words += len(sentence)

            for word in sentence:
                word = word.lower()
                if word not in self.word_counts:
                    misspellings += 1

        return (total_words - misspellings) / total_words

    def words(self, text):
        """
        :return: array with every word(in lower case) in the argument containing a-z
        """
        return re.findall('[a-z]+', text.lower())

    def train(self, dictionary_path='/data/train_data/dictionary.txt',
              train_path='/data/train_data/bigGutenbergSample.txt'):

        # first we fill in the dictionary to our word_counts starting every word off with one occurrence
        with open(dictionary_path) as dictionary_file:
            dictionary = self.words(dictionary_file.read())

        for dict_entry in dictionary:
            if dict_entry not in self.word_counts:
                self.word_counts[dict_entry] = 0
            self.word_counts[dict_entry] += 1

        # now we train a bit with actual text for word occurrence numbers
        with open(train_path) as train_file:
            training_corpus = self.words(train_file.read())

        for word in training_corpus:
            if word not in self.word_counts:
                self.word_counts[word] = 0
            self.word_counts[word] += 1

    def score(self, data):
        return self.spelling_analysis(data)


if __name__ == '__main__':
    spell = Spelling()
    spell.train(dictionary_path='../data/train_data/dictionary.txt',
              train_path='../data/train_data/bigGutenbergSample.txt')
    print(
        spell.score(["This sentence has sumething misspelled in it".split(), "This is just another sentence".split()]))

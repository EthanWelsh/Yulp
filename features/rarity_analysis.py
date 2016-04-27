import re

from model.feature import Feature

"""
dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010.
<http://wordnet.princeton.edu>

"""


class Rarity(Feature):
    def __init__(self):
        self.word_counts = {}
        self.max_word_occurrences = 0

    def rarity_analysis(self, text):
        """
        :return: a value between 0 and 1 representing the average rarity value per word
        """

        input_len = 0
        total_sent_count = 0

        for sent in text:
            input_len += len(sent)
            for word in sent:
                word = word.lower()
                word = word.strip('.!?"@#$%^&*(){[]}<>')
                if word in self.word_counts:
                    total_sent_count += self.word_counts[word]

        return (total_sent_count / input_len) / self.max_word_occurrences if self.max_word_occurrences > 0 else 0.0

    @staticmethod
    def words(text):
        """
        :return: list with every word(in lower case) in the argument containing a-z
        """
        return re.findall('[a-z]+', text.lower())

    def train(self, dictionary_path='/data/train_data/dictionary.txt',
                    train_path='/data/train_data/bigGutenbergSample.txt'):
        """
        :return: a model with each features unique word's number of occurrences
        """

        # First we'll put in every word in the dictionary
        with open(dictionary_path, 'r') as dictionary_file:
            dictionary = self.words(dictionary_file.read())

        for dict_entry in dictionary:
            if dict_entry not in self.word_counts:
                self.word_counts[dict_entry] = 0
            self.word_counts[dict_entry] += 1

        # now we train a bit with actual text for word occurrence numbers
        with open(train_path, 'r', encoding='utf-8') as train_file:
            training_corpus = self.words(train_file.read())

        for word in training_corpus:
            if word not in self.word_counts:
                self.word_counts[word] = 0
            self.word_counts[word] += 1
            if self.word_counts[word] > self.max_word_occurrences:
                self.max_word_occurrences = self.word_counts[word]

    def score(self, data):
        return self.rarity_analysis(data)


if __name__ == '__main__':
    rarity = Rarity()
    print("Llllllllllllll")
    rarity.train(dictionary_path='../data/train_data/dictionary.txt',
                 train_path='../data/train_data/bigGutenbergSample.txt')
    print(rarity.score([
        "This sentence has sumthing misspelled in it".split(),
        "This is just another sentence".split()]))

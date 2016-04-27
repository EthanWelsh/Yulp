import re

from model.feature import Feature

"""
dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010.
<http://wordnet.princeton.edu>

"""


class Readability(Feature):
    def __init__(self):
        self.dale_chall_easy_words = {}

    def readability_analysis(self, text):
        """
        :return: a tuple with three values between 0 and 1 representing the coleman liau, dale chall and flesch kincaid
        indices mapped between 0 and 1. 1 represents very difficult to read, 0 represents easy to read
        """

        total_chars = 0
        total_words = 0
        total_sentences = 0
        total_difficult_words = 0
        total_syllables = 0

        for sentence in text:
            total_sentences += 1
            for word in sentence:
                word = word.lower()
                word = word.strip('.!?"@#$%^&*(){[]}<>')
                total_words += 1
                total_syllables += self.syllables(word)
                if word not in self.dale_chall_easy_words:
                    total_difficult_words += 1
                total_chars += len(word)

        avg_letter_per_word = total_chars / total_words
        avg_word_per_sentence = total_words / total_sentences

        if avg_word_per_sentence != 0:
            coleman_liau_index = (0.0588 * avg_letter_per_word * 100) - (0.296 * (100 / avg_word_per_sentence)) - 15.8
            coleman_liau_index_mapped = coleman_liau_index / 12
        else:
            coleman_liau_index_mapped = 0.0

        if total_words != 0 and total_sentences != 0:
            dale_chall_index = 0.1579 * ((total_difficult_words / total_words) * 100) + 0.0496 * (
            total_words / total_sentences)
            dale_chall_index_mapped = dale_chall_index / 10
        else:
            dale_chall_index_mapped = 0.0

        if total_sentences != 0 and total_words != 0:
            flesch_kincaid_index = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (
            total_syllables / total_words)
            flesch_kincaid_index_mapped = ((flesch_kincaid_index - 0) / (100 - 0) * (1))
        else:
            flesch_kincaid_index_mapped = 0.0

        return (dale_chall_index_mapped, coleman_liau_index_mapped, flesch_kincaid_index_mapped)

    def words(self, text):
        """
        :return: array with every word(in lower case) in the argument containing a-z
        """
        return re.findall('[a-z]+', text.lower())

    def train(self, dale_chall_easy_words_path='data/train_data/DaleChallEasyWordList.txt'):
        with open(dale_chall_easy_words_path, 'r') as dale_chall_easy_words_file:
            self.dale_chall_easy_words = self.words(dale_chall_easy_words_file.read())

    def score(self, data):
        return self.readability_analysis(data)

    def syllables(self, word):
        """
        Need to make sure that I only input all lowercase words only letters
        """
        vowel_str = 'aeiouy'
        syllable_count = 0
        if word[0] in vowel_str:
            syllable_count += 1
        for a in range(1, len(word)):
            if word[a] in vowel_str and word[a - 1] not in vowel_str:
                syllable_count += 1

        if syllable_count == 0:
            syllable_count += 1
        if word.endswith('e'):
            syllable_count -= 1
        if word.endswith('le'):
            syllable_count += 1

        return syllable_count


if __name__ == '__main__':
    cl = Readability()
    cl.train(dale_chall_easy_words_path='../data/train_data/DaleChallEasyWordList.txt')
    print(cl.score([
        "this is a simple test sentence".split(),
        "This is just so that we can confirm that they are screwing up".split(),
        "Maybe placing higher scores is an issue".split(),
        "Finally I will use this sentence for the last one.".split()]))

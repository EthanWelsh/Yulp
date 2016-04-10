import re
import string

from model.feature import Feature

"""
dictionary source:
Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
"""


class Spelling(Feature):

    def __init__(self):
        self.word_counts = {}

    def spelling_analysis(self, text):
        """
        This function returns a value between 0 and 1 representing the proportion of correctness
        :return: 1 is everything spelled correctly, 0 is everything spelled incorrectly
        """

        misspellings = 0
        total_words = len(text)
        for word in text:
            word = word.lower()
            if self.word_counts.get(word) is None:
                print("we didn't find: ", word)
                misspellings += 1
        return (total_words - misspellings) / total_words

    # TODO Update method signature to comply with Feature class
    def train(self, features):
        for f in features:
            self.word_counts[f] = self.word_counts.get(f, 0) + 1

    def known(self, words):
        return set(w for w in words if w in self.word_counts)

    @staticmethod
    def words(text):
        """
        This function returns an array with every word(in lower case) in the argument containing a-z
        """
        return re.findall('[a-z]+', text.lower())

    @staticmethod
    def edits1(word):
        word = word.lower()
        s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in s if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in s for c in string.ascii_lowercase if b]
        inserts = [a + c + b for a, b in s for c in string.ascii_lowercase]
        return set(deletes + transposes + replaces + inserts)

    @staticmethod
    def known_edits2(self, word):
        return set(e2 for e1 in Spelling.edits1() for e2 in Spelling.edits1() if e2 in self.word_counts)

    def correct(self, word):

        # candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
        likeliest = ['No Match', 0]
        possibilities = Spelling.edits1()

        for word in possibilities:
            word = word.lower()
            print(word)

            if self.word_counts.get(word) is not None:
                print("word:", word, " ", self.word_counts[word])

                if self.word_counts[word] > likeliest[1]:
                    likeliest = [word, self.word_counts[word]]
                    print("likeliest is now ", word, " with occurrences: ", self.word_counts[word])

        return likeliest[0]

    def score(self, data):
        print("data: ", data)
        return Spelling.spelling_analysis(data)

if __name__ == '__main__':
    spell = Spelling()

    with open('../data/train_data/dictionary.txt', 'r') as dictionary_file:
        spell.train(spell.words(dictionary_file.read()))

    with open('../data/train_data/bigGutenbergSample.txt', 'r') as train_file:
        spell.train(spell.words(train_file.read()))

    print(spell.score(["This", "has", "sumthing", "wrong", "in", "it"]))

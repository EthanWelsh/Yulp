# dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
import re, collections
from model.feature import Feature


class Spelling(Feature):
    def __init__(self):
        self.word_counts = {}
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # This function returns a value between 0 and 1 representing the proportion of correctness
    # 1 is everything spelled correctly, 0 is everything spelled incorrectly
    def spelling_analysis(self, text):
        misspellings = 0
        totalWords = 0
        for sentence in text:
            totalWords += len(sentence)
            for word in sentence:
                word = word.lower()
                if word not in self.word_counts:
                    misspellings += 1
                    print(self.correct(word))
        return (totalWords - misspellings) / totalWords

    # this function returns an array with every word(in lower case) in the argument containing a-z
    def words(self, text):
        return re.findall('[a-z]+', text.lower())

    # this function returns a model with each features unique word's number of occurrences
    def train(self):
        #first we fill in the dictionary to our word_counts starting every word off with one occurrence
        dictionaryFile = open('../data/train_data/dictionary.txt', 'r')
        dictionary = self.words(dictionaryFile.read())
        for dict_entry in dictionary:
            if dict_entry not in self.word_counts:
                self.word_counts[dict_entry] = 0
            self.word_counts[dict_entry] += 1

        # now we train a bit with actual text for word occurrence numbers
        trainFile = open('../data/train_data/bigGutenbergSample.txt', 'r')
        training_corpus = self.words(trainFile.read())
        for word in training_corpus:
            if word not in self.word_counts:
                self.word_counts[word] = 0
            self.word_counts[word] += 1

    def edits1(self, word):
        word = word.lower()
        s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in s if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in s for c in self.alphabet if b]
        inserts = [a + c + b for a, b in s for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.word_counts)

    def known(self, words):
        return set(w for w in words if w in self.word_counts)

    def correct(self, word):
        # candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
        likeliest = ['No Match', 0]
        possibilities = self.edits1(word)
        # print("POSSIBILITIES: ",possibilities)
        for word in possibilities:
            word = word.lower()
            #print(word)
            if self.word_counts.get(word) != None:
                #print("word:", word, " ", self.word_counts[word])
                if self.word_counts[word] > likeliest[1]:
                    likeliest = [word, self.word_counts[word]]
                    #print("likeliest is now ", word, " with occurrences: ", self.word_counts[word])
        return likeliest[0]

    def score(self, data):
        return self.spelling_analysis(data)


#this only happens when we run from the script
if __name__ == '__main__':
    spell = Spelling()
    spell.train()
    print(spell.score(["This sentence has sumething misspelled in it".split(), "This is just another sentence".split()]))

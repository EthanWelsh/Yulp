#dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
import re, collections
from model.feature import Feature
class Rarity(Feature):


    def __init__(self):
        self.word_counts = {}
        self.max_word_occurrences = 0

    #This function returns a value between 0 and 1 representing the average rarity value per word
    def rarity_analysis(self, text):
        input_len = 0
        total_sent_occurrence_count = 0
        for sent in text:
            input_len += len(sent)
            for word in sent:
                if word in self.word_counts:
                    total_sent_occurrence_count += self.word_counts[word]

        return (total_sent_occurrence_count / input_len) / self.max_word_occurrences if self.max_word_occurrences > 0 else 0.0
        #return -1


    #this function returns list with every word(in lower case) in the argument containing a-z
    def words(self, text):
        return re.findall('[a-z]+', text.lower())

    #this function returns a model with each features unique word's number of occurrences
    def train(self):
        #First we'll put in every word in the dictionary
        dictionaryFile = open('../data/train_data/dictionary.txt', 'r')
        dictionary = rarity.words(dictionaryFile.read())
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
            if self.word_counts[word] > self.max_word_occurrences:
                self.max_word_occurrences = self.word_counts[word]

    def score(self, data):
        return Rarity.rarity_analysis(self, data)


#this only happens when we run from the script
if __name__ == '__main__':
    rarity = Rarity()
    rarity.train()
    print(rarity.score(["This sentence has sumthing misspelled in it".split(), "This is just another sentence".split()]))

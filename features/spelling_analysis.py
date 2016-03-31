#dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
import re, collections
from model.feature import Feature
class Spelling(Feature):
    wordCounts = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        print("created a spelling object")

    #This function returns a value between 0 and 1 representing the proportion of correctness
    #1 is everything spelled correctly, 0 is everything spelled incorrectly
    def spelling_analysis(self, text):
        misspellings = 0
        totalWords = len(text)
        for word in text:
            word = word.lower()
            if(Spelling.wordCounts.get(word) == None):
                print("we didn't find: ", word)
                misspellings += 1
        return (totalWords - misspellings) / totalWords


    #this function returns an array with every word(in lower case) in the argument containing a-z
    def words(self, text):
        return re.findall('[a-z]+', text.lower())

    #this function returns a model with each features unique word's number of occurrences
    def train(self, features):
        #print(features)
        model = Spelling.wordCounts
        for f in features:
            if(model.get(f) == None):
                model[f] = 0
            model[f] = model[f] + 1
        #print(model)
        return model

    def edits1(self, word):
        word = word.lower()
        s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in s if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in s for c in Spelling.alphabet if b]
        inserts    = [a + c + b for a, b in s for c in Spelling.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in Spelling.edits1(word) for e2 in Spelling.edits1(e1) if e2 in Spelling.wordCounts)

    def known(self, words):
        return set(w for w in words if w in Spelling.wordCounts)

    def correct(self, word):
        #candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
        likeliest = ['No Match', 0]
        possibilities = Spelling.edits1(word)
        #print("POSSIBILITIES: ",possibilities)
        for word in possibilities:
            word = word.lower()
            print(word)
            if Spelling.wordCounts.get(word) != None:
                print("word:", word, " ",Spelling.wordCounts[word])
                if Spelling.wordCounts[word] > likeliest[1]:
                    likeliest = [word, Spelling.wordCounts[word]]
                    print("likeliest is now ", word, " with occurrences: ",Spelling.wordCounts[word])
        return likeliest[0]

    def score(self, data):
        print("data: ", data)
        return Spelling.spelling_analysis(self, data)

spell = Spelling()
dictionaryFile = open('../data/train_data/dictionary.txt', 'r')
wordCounts = spell.train(spell.words(dictionaryFile.read()))

#now we train a bit with actual text for word occurrence numbers
trainFile = open('../data/train_data/bigGutenbergSample.txt', 'r')
wordCounts = spell.train(spell.words(trainFile.read()))
#print("wordCounts: ", wordCounts)
print(spell.score(["This", "has", "sumthing", "wrong", "in", "it"]))
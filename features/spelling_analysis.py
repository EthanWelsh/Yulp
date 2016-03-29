#dictionary source: Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
import re, collections

wordCounts = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#This function returns a value between 0 and 1 representing the proportion of correctness
#1 is everything spelled correctly, 0 is everything spelled incorrectly
def spelling_analysis(text):
    misspellings = 0
    totalWords = len(text)
    for word in text:
        word = word.lower()
        if(wordCounts.get(word) == None):
            print("we didn't find: ", word)
            misspellings += 1
    return (totalWords - misspellings) / totalWords


#this function returns an array with every word(in lower case) in the argument containing a-z
def words(text):
    return re.findall('[a-z]+', text.lower())

#this function returns a model with each features unique word's number of occurrences
def train(features):
    #print(features)
    model = wordCounts
    for f in features:
        if(model.get(f) == None):
            model[f] = 0
        model[f] = model[f] + 1
    #print(model)
    return model

def edits1(word):
    word = word.lower()
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in wordCounts)

def known(words):
    return set(w for w in words if w in wordCounts)

def correct(word):
    #candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    likeliest = ['No Match', 0]
    possibilities = edits1(word)
    #print("POSSIBILITIES: ",possibilities)
    for word in possibilities:
        word = word.lower()
        print(word)
        if wordCounts.get(word) != None:
            print("word:", word, " ",wordCounts[word])
            if wordCounts[word] > likeliest[1]:
                likeliest = [word, wordCounts[word]]
                print("likeliest is now ", word, " with occurrences: ",wordCounts[word])
    return likeliest[0]

#first we add every word in the dictionary to our wordCounts list
dictionaryFile = open('../data/train_data/dictionary.txt', 'r')
wordCounts = train(words(dictionaryFile.read()))

#now we train a bit with actual text for word occurrence numbers
trainFile = open('../data/train_data/bigGutenbergSample.txt', 'r')
wordCounts = train(words(trainFile.read()))


#print(edits1("Ibcorrect"))
#print(known_edits2("Ibcorrect"))
#print("known: ",known("an"))

#print(wordCounts)
print(spelling_analysis(["This", "has", "nothing", "wrong", "in", "it"]))
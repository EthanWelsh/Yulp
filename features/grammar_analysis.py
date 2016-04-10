import collections
import re
from model.feature import Feature
import string


class GrammarScore(Feature):
    def train(features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    @staticmethod
    def spelling_analysis(text):
        """
        This function returns a value between 0 and 1 representing the grammatical correctness of the input text
        """
        return 0

    @staticmethod
    def words(text):
        return re.findall('[a-z]+', text.lower())

    @staticmethod
    def edits1(word):
        s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in s if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in s for c in alphabet if b]
        inserts = [a + c + b for a, b in s for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    @staticmethod
    def known_edits2(word):
        return set(e2 for e1 in GrammarScore.edits1(word) for e2 in GrammarScore.edits1(e1) if e2 in NWORDS)

    @staticmethod
    def known(words):
        return set(w for w in words if w in NWORDS)

    @staticmethod
    def correct(word):
        candidates = GrammarScore.known([word]) or \
                     GrammarScore.known(GrammarScore.edits1(word)) or \
                     GrammarScore.known_edits2(word) or [word]
        return max(candidates, key=NWORDS.get)


if __name__ == '__main__':
    gs = GrammarScore()
    alphabet = string.ascii_lowercase

    with open('/yulp/data/train_data/bigGutenbergSample.txt') as data:
        NWORDS = gs.train(gs.words(data.read()))

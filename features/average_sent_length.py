from model.feature import Feature
from nltk.tokenize import sent_tokenize


class AverageSentLength(Feature):
    def train(self):
        pass

    def score(self, data):
        total_lens = 0

        for sentence in data:
            total_lens += len(sentence)

        return total_lens / len(data)

    def load(self, path):
        pass

    def save(self, path):
        pass

if __name__ == '__main__':
    asl = AverageSentLength()
    print(asl.score(['Hello world, it is nice to meet you.'.split(),
                     'I\'m Mick.'.split(),
                     'I am a CS major.'.split(),
                     'Goodbye.'.split()]))

from model.feature import Feature
from nltk.tokenize import sent_tokenize


class AverageSentLength(Feature):
    def train(self, data, labels):
        pass

    def score(self, data):
        sentences = sent_tokenize(data)   # sent_tokenize() returns a list of sentences created from the given data
        total_lens = 0

        for sentence in sentences:
            total_lens += len(sentence)

        return total_lens / len(sentences)

    def load(self, path):
        pass

    def save(self, path):
        pass


if __name__ == '__main__':
    asl = AverageSentLength()
    print(asl.score(['Hello world, it is nice to meet you. I\'m Mick. I am a CS major. Goodbye.']))

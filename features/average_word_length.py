from model.feature import Feature


class AverageWordLength(Feature):
    def train(self, data, labels):
        pass

    def score(self, data):
        average_length = 0
        word_count = 0

        for sentence in data:
            for word in sentence:
                average_length += len(word)
                word_count += 1

        return average_length/word_count if word_count > 0 else 0

    def load(self, path):
        pass

    def save(self, path):
        pass


if __name__ == '__main__':
    awl = AverageWordLength()
    print(awl.score([['Hello', 'world'], ['Nice', 'to', 'meet', 'you']]))


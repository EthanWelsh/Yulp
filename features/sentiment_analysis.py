from nltk.sentiment.vader import SentimentIntensityAnalyzer
from model.feature import Feature


class SentimentAnalysis(Feature):

    def __init__(self):
        self.intensity_analyzer = SentimentIntensityAnalyzer()

    def save(self, path):
        pass

    def load(self, path):
        pass

    def train(self):
        pass

    def score(self, text):

        if isinstance(text, list):
            text = ' '.join(text)

        scores = self.intensity_analyzer.polarity_scores(text)
        return scores['compound']


if __name__ == '__main__':
    sa = SentimentAnalysis()
    print(sa.score('I really hate this place'))
    print(sa.score('Such a good place to grab a meal!'))

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from model.feature import Feature


class SentimentAnalysis(Feature):

    def __init__(self):
        self.intensity_analyzer = SentimentIntensityAnalyzer()

    def score(self, text):
        scores = self.intensity_analyzer.polarity_scores(text)
        return scores['compound']

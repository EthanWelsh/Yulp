from nltk.sentiment.vader import SentimentIntensityAnalyzer
from model.feature import Feature


intensityAnalyzer = None


class SentimentAnalysis(Feature):

    def score(self, text):
        global intensityAnalyzer
        if intensityAnalyzer is None:
            intensityAnalyzer = SentimentIntensityAnalyzer()
        scores = intensityAnalyzer.polarity_scores(text)
        return scores['compound']

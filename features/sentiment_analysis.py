from nltk.sentiment.vader import SentimentIntensityAnalyzer


intensityAnalyzer = None


def sentiment_analysis(text):
    global intensityAnalyzer
    if intensityAnalyzer is None:
        intensityAnalyzer = SentimentIntensityAnalyzer()
    scores = intensityAnalyzer.polarity_scores(text)
    return scores['compound']

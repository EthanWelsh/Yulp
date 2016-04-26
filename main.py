import json
import random

from features import average_word_length, sentiment_analysis, rarity_analysis
from model.feature import FeatureVector
from model.svm import SVM


def retrieve_reviews(n):

    reviews = []

    with open('data/reviews.json') as reviews_file:
        lines = reviews_file.readlines()

        for index in range(len(lines)):
            review_json = random.choice(lines)

            if index > n:
                break

            parsed_review = json.loads(review_json)
            reviews.append((parsed_review['text'], parsed_review['price']))

    return reviews


def main():
    vector = FeatureVector()

    vector.append(average_word_length.AverageWordLength())
    vector.append(sentiment_analysis.SentimentAnalysis())
    vector.append(rarity_analysis.Rarity())

    vector.train()

    model = SVM(vector)

    reviews = retrieve_reviews(1000)

    train_reviews = reviews[:950]
    test_reviews = reviews[950:]

    text, labels = zip(*train_reviews)
    model.train(text, labels)

    text, labels = zip(*test_reviews)

    matches = 0

    for i in range(len(labels)):
        if model.predict(text[i]) == test_reviews[i][1]:
            matches += 1

    print('Accuracy = {}%'.format((matches/len(reviews)) * 100))


if __name__ == '__main__':
    main()

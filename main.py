import json
import random

from features import average_word_length, sentiment_analysis, rarity_analysis
from model.feature import FeatureVector
from model.svm import SVM


def retrieve_reviews(n, data_path='data/reviews.json'):

    reviews = []

    with open(data_path) as reviews_file:
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

    # Add features into feature vector
    vector.append(average_word_length.AverageWordLength())
    vector.append(sentiment_analysis.SentimentAnalysis())
    vector.append(rarity_analysis.Rarity())

    # Train all of the features individually
    vector.train([], [])

    model = SVM(vector)

    # Retrieve 1000 random reviews and associated costs
    reviews = retrieve_reviews(1000)

    # Split reviews into a training and testing portion
    train_reviews = reviews[:950]
    test_reviews = reviews[950:]

    # Separate text and label to use during the training process
    text, labels = zip(*train_reviews)
    model.train(text, labels)

    # Separate text and label to use during the testing process
    text, labels = zip(*test_reviews)

    matches = 0
    distance = {}

    for i in range(len(labels)):
        predicted_score = model.predict(text[i])
        actual_score = labels[i]

        # count how many predicted scores match with the actual ones
        if predicted_score == actual_score:
            matches += 1

        # get a histogram of how far predicted scores differ from the actual
        dist = abs(predicted_score - actual_score)
        distance[dist] = distance.get(dist, 0) + 1

    print('Matches = {0:.2f}%'.format((matches/len(labels)) * 100))

    for distance, count in distance.items():
        print("{} : {}".format(distance, count))


if __name__ == '__main__':
    main()

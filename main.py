from features import average_word_length, sentiment_analysis, rarity_analysis, tfidf
from model.feature import FeatureVector
from model.svm import SVM
from util.parse_reviews import retrieve_reviews


def main():
    # Retrieve 1000 random reviews and associated costs
    reviews = retrieve_reviews(1000)

    # Split reviews into a training and testing portion
    train_reviews = reviews[:950]
    test_reviews = reviews[950:]

    # Separate text and label to use during the training process
    text, labels = zip(*train_reviews)

    vector = FeatureVector()

    # Add features into feature vector
    vector.append(average_word_length.AverageWordLength())
    vector.append(sentiment_analysis.SentimentAnalysis())
    vector.append(rarity_analysis.Rarity())
    vector.append(tfidf.TfIdf())

    # Train all of the features individually
    vector.train(text, labels)

    model = SVM(vector)
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

    print('Matches = {0:.2f}%'.format((matches / len(labels)) * 100))

    for distance, count in distance.items():
        print("{} : {}".format(distance, count))


if __name__ == '__main__':
    main()

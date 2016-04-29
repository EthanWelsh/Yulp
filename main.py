from features import average_word_length, sentiment, rarity, tfidf, readability, spelling, food_sophistication, \
    sentence_topic
from model.feature import FeatureVector
from model.svm import SVM
from util.parse_reviews import retrieve_reviews


def main():

    reviews = retrieve_reviews(5000)

    # Split reviews into a training and testing portion
    train_reviews = reviews[:4500]
    test_reviews = reviews[4500 + 1:]

    # Separate text and label to use during the training process
    text, labels = zip(*train_reviews)

    vector = FeatureVector()

    # Add features into feature vector
    vector.append(sentiment.SentimentAnalysis())
    vector.append(tfidf.TfIdf())
    vector.append(readability.Readability())
    vector.append(food_sophistication.FoodSophistication())
    vector.append(average_word_length.AverageWordLength())
    vector.append(rarity.Rarity())
    vector.append(spelling.Spelling())
    vector.append(sentence_topic.SentenceTopic())

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

    print('Matches = {:.2%}'.format(matches / len(labels)))

    for distance, count in distance.items():
        print("{} : {}".format(distance, count))


if __name__ == '__main__':
    main()

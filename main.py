from features import average_word_length, sentiment_analysis
from model.feature import FeatureVector
from model.svm import SVM


def main():
    vector = FeatureVector()

    vector.append(average_word_length.AverageWordLength())
    vector.append(sentiment_analysis.SentimentAnalysis())

    review_a = ['Disgusting, filthy, and criminally slow'.split(),
                'Awful place, never ever go there'.split(),
                'Abominable, to put it simply. Our ratatouille was quite simply wretched.'.split()]

    review_b = ['Its really good'.split(),
                'Nice food. Good service'.split()]

    vector.train()

    model = SVM(vector)
    model.train(reviews=[review_a, review_b], labels=[1, 4])

    print(model.predict(data=review_a))
    print(model.predict(data=review_b))


if __name__ == '__main__':
    main()

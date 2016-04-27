from itertools import chain

import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import Normalizer

from model.feature import Feature
from util.parse_reviews import retrieve_reviews


class TfIdf(Feature):
    def __init__(self):
        self.kbest = None
        self.vect = None
        self.truncated = None
        self.normalizer = None

    def train(self, reviews, labels):
        self.vect = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words='english')

        reviews_text = [' '.join(list(chain.from_iterable(review))) for review in reviews]
        tfidf_matrix = self.vect.fit_transform(reviews_text).toarray()

        self.truncated = TruncatedSVD(n_components=50)
        self.truncated.fit(tfidf_matrix, labels)

        trunc = self.truncated.transform(tfidf_matrix)
        self.normalizer = Normalizer()
        self.normalizer.fit(trunc)

        self.kbest = SelectKBest(f_classif, k=5)
        self.kbest.fit(self.normalizer.transform(trunc), labels)

    def score(self, data):
        reviews_text = ' '.join(list(chain.from_iterable(data)))
        tfidf_matrix = self.vect.transform([reviews_text]).toarray()

        trunc = self.truncated.transform(tfidf_matrix)

        return tuple(self.kbest.transform(self.normalizer.transform(trunc))[0, :])


if __name__ == '__main__':
    reviews = retrieve_reviews(100, data_path='../data/reviews.json')
    reviews, labels = zip(*reviews)
    feat = TfIdf()

    feat.train(reviews, labels)
    print(feat.score(reviews[0]))

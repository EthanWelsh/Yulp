from itertools import chain

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from model.feature import Feature

from main import retrieve_reviews


class TfIdf(Feature):

    def __init__(self):
        self.kbest = None
        self.vect = None

    def train(self, reviews, labels):
        self.vect = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words='english')

        reviews_text = [' '.join(list(chain.from_iterable(review))) for review in reviews]
        tfidf_matrix = self.vect.fit_transform(reviews_text).toarray()

        self.kbest = SelectKBest(chi2, k=5).fit(tfidf_matrix, labels)

    def score(self, data):
        reviews_text = ' '.join(list(chain.from_iterable(data)))
        tfidf_matrix = self.vect.transform([reviews_text]).toarray()
        print(self.kbest.transform(tfidf_matrix))

if __name__ == '__main__':

    reviews = retrieve_reviews(100, data_path='../data/reviews.json')
    reviews, labels = zip(*reviews)
    feat = TfIdf()

    feat.train(reviews, labels)
    feat.score(reviews[0])





from sklearn.feature_extraction.text import TfidfVectorizer

from model.feature import Feature


class TfIdf(Feature):
    def train(self):
        pass

    def score(self, data):
        pass


if __name__ == '__main__':
    vect = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), stop_words='english')

    tfidf_matrix = vect.fit_transform([open('/Users/welshej/Desktop/CS1653/lec.org').read(),
                                       open('/Users/welshej/Desktop/PHYS87/lec.org').read()])

    print(vect.get_feature_names())
    print(tfidf_matrix.shape)




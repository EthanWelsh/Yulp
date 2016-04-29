from model.feature import Feature
from scipy import mean


def normalize_key(key):
    """Normalize a key to a string"""
    if isinstance(key, int):
        return str(key)
    return key


class FoodWord(object):
    """
    Represents a "food word" that we are tracking

    Used to calculate the number of times a word was used in each price
    category, and to generate the most likely category based on past usage
    """
    def __init__(self, word):
        # Keep a reference to the work being represented
        self.word = word

        # Build a dictionary to track the number of times used at each price
        # level
        self.dictionary = dict()
        self.dictionary['1'] = 0
        self.dictionary['2'] = 0
        self.dictionary['3'] = 0
        self.dictionary['4'] = 0

    def __getitem__(self, key):
        key = normalize_key(key)
        return self.dictionary[key]

    def __setitem__(self, key, value):
        key = normalize_key(key)
        self.dictionary[key] = value

    @property
    def most_likely_price(self):
        best_key = None
        best_value = 0
        for (key, value) in self.dictionary.items():
            if value > best_value:
                best_key = key
                best_value = value
        if best_key is None:
            return None
        else:
            return int(best_key)


class FoodSophistication(Feature):

    def __init__(self):
        self.food_word_dict = dict()
        food_types = self._get_food_types()
        for item in food_types:
            item = item.lower()
            if len(item.split(' ', 1)) == 2:
                continue
            elif item not in self.food_word_dict:
                self.food_word_dict[item] = FoodWord(item)

    def train(self, reviews, prices):
        """
        Train the model on the prices and reviews provided

        Takes the prices and reviews and builds out the lookup table

        Arguments:
            reviews: a list of reviews
            prices: a list of prices

            The two lists should be parallel, such that prices[0] corresponds
                with reviews[0]

        Returns:
            None
        """
        training_data = zip(prices, reviews)
        for price, review in training_data:
            for sentence in review:
                for word in sentence:
                    word = word.lower()
                    if word in self.food_word_dict:
                        self.food_word_dict[word][price] += 1

    def score(self, review):
        """
        Score a single review

        Arguments:
            list(list(str)): the review to score
        Returns:
            tuple(float): the score for the review
        """
        scores = map(lambda sentence: self._score_one_sentence(sentence),
                     review)
        return (mean(list(scores)), )

    def _score_one_sentence(self, sentence):
        """Score a single sentence"""
        sentence = map(lambda word: word.lower(), sentence)
        food_words = filter(lambda word: word in self.food_word_dict,
                            sentence)
        scores = map(lambda word: self.food_word_dict[word].most_likely_price,
                     food_words)
        scores = list(scores)
        if len(scores) == 0:
            return 0
        else:
            return mean(scores)

    def _get_food_types(self, food_words_path='data/food_words.txt'):
        """
        Get the list of food types

        Returns:
            set(<str>): the set of words
        """
        words = set()
        with open(food_words_path, encoding='utf-8') as f:
            for line in f.readlines():
                words.add(line)
        return words

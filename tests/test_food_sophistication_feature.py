from features.food_sophistication import FoodWord, FoodSophistication


class FoodSophisticationTestClass(FoodSophistication):

    def _get_food_types(self):
        s = set()
        s.add('foo')
        s.add('bar')
        s.add('foo bar')
        return s


class TestFoodWordClass:

    def test_it_stores_values_for_each_price(self):
        fw = FoodWord('test')
        assert fw[1] == 0
        assert fw[2] == 0
        assert fw[3] == 0
        assert fw[4] == 0

    def test_it_can_reassign_price_values(self):
        fw = FoodWord('test')
        fw[1] += 1
        assert fw[1] == 1

    def test_it_can_get_the_most_likely_price(self):
        fw = FoodWord('test')
        assert fw.most_likely_price is None

        fw[1] = 1
        fw[2] = 2
        fw[3] = 3
        assert fw.most_likely_price == 3


class TestFoodSophisticationFeature:

    def test_it_removes_multi_word_food_items(self):
        feature = FoodSophisticationTestClass()
        assert len(feature.food_word_dict.items()) == 2

    def test_it_can_score_a_review(self):
        feature = FoodSophisticationTestClass()
        reviews = [
            [['Foo']], [['Foo']], [['Foo']], [['Foo']]
        ]
        prices = [
            1, 1, 3, 4
        ]
        feature.train(reviews, prices)
        assert feature.score([['Foo']]) == 1
        assert feature.score([['Foo', 'baz']]) == 1

    def test_it_averages_score_of_all_words_in_sentence(self):
        feature = FoodSophisticationTestClass()
        reviews = [
            [['Foo']], [['Foo']], [['Bar']], [['Bar']]
        ]
        prices = [
            1, 1, 3, 3
        ]
        feature.train(reviews, prices)
        assert feature.score([['Foo', 'bar']]) == 2

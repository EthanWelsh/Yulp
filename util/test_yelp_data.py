import os
from yelp_data import Business, Review

TEST_DATA_DIRECTORY = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../test_data'
)


class TestJSONParsing:

    def setup_method(self, method):
        Review._business_id_to_reviews = dict()
        Business._business_id_to_business = dict()
        self.businesses = Business.create_from_file(
            '{}/business-json-structure.json'.format(TEST_DATA_DIRECTORY)
        )
        self.reviews = Review.create_from_file(
            '{}/review-json-structure.json'.format(TEST_DATA_DIRECTORY)
        )

    def teardown_method(self, method):
        self.businesses = None
        self.reviews = None

    def test_creates_businesses_objects_correctly_from_file(self):
        first = self.businesses[0]
        assert first._business_id == '5UmKMjUEUNdYWqANhGckJw'
        assert first.price_score == 1
        assert len(Business._business_id_to_business.keys()) == 2

    def test_creates_review_objects_correctly_from_file(self):
        first = self.reviews[0]
        assert first._business_id == '5UmKMjUEUNdYWqANhGckJw'
        assert isinstance(first.text, str)
        assert len(
            Review._business_id_to_reviews[first._business_id]
        ) == 2

    def test_links_business_to_reviews(self):
        first = self.businesses[0]
        assert len(first.reviews) == 2
        assert first.reviews[0] == self.reviews[0]

    def test_links_review_to_business(self):
        review = self.reviews[0]
        business = self.businesses[0]
        assert review.business == business

import json


class BaseYelpData:

    def __init__(self, data):
        pass

    @classmethod
    def create_from_file(cls, file_path):
        """
        Create data from a file

        Parse the given data file and return a `list` of objects of this type

        :param file_path: the file to read from
        :returns: list of parsed data
        """
        objects = list()
        with open(file_path) as f:
            for line in f.readlines():
                parsed_json = json.loads(line)
                objects.append(cls(parsed_json))
        return objects


class Business(BaseYelpData):

    _business_id_to_business = dict()
    """Look up a business by its ID"""

    def __init__(self, data):
        self._business_id = data['business_id']
        """The ID of this business"""

        self.price_score = data['attributes']['Price Range']
        """The price score for this business"""

        Business._business_id_to_business[self._business_id] = self

    @property
    def reviews(self):
        """The reviews for this business"""
        return Review._business_id_to_reviews[self._business_id]


class Review(BaseYelpData):

    _business_id_to_reviews = dict()
    """Lookup reviews by their business ID"""

    def __init__(self, data):
        self._business_id = data['business_id']
        """The ID of the business that this review belongs to"""

        self.text = data['text']
        """The text of the review"""

        if self._business_id not in Review._business_id_to_reviews:
            Review._business_id_to_reviews[self._business_id] = list()
        Review._business_id_to_reviews[self._business_id].append(self)

    @property
    def business(self):
        """The business for this review"""
        return Business._business_id_to_business[self._business_id]

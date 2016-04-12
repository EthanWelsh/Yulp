import json
from nltk.tokenize import sent_tokenize


def get_reviews_in_range(min, max):
    # 1. read in the json corpus of reviews, saving the review text and dollar sign rating

    data_file = open("yelp_academic_dataset_business.json")
    business_data = {}

    for line in data_file:
        data = json.loads(line)
        business_id = data["business_id"]
        name = data["name"]
        categories = data["categories"]
        attributes = data["attributes"]

        if len(categories) > 0:
            if "Restaurants" in categories:
                try:
                    price_range = attributes["Price Range"]
                    business_data[business_id] = [name, categories, price_range]
                except KeyError:
                    price_range = "NA"

    review_file = open("yelp_academic_dataset_review.json")
    review_data = []
    for line in review_file:
        data = json.loads(line)
        business_id = data["business_id"]
        text = data["text"]

        if business_id in business_data:
            review_data[business_id] = text

    # 2. get a list of the tokenized reviews with dollar sign scores within the min-max range

    reviews_in_range = []

    for key, business in enumerate(business_data):
        if min <= business[2] <= max:
            reviews_in_range.append(review_data[key])

    # 3. sentence tokenize the reviews

    tokenized_reviews = []

    for review in reviews_in_range:
        tokenized_reviews.append(sent_tokenize(review))

    return tokenized_reviews

import json

import sys
from nltk import sent_tokenize


def business_id_to_price(buisness_dataset_path):
    prices = {}

    with open(buisness_dataset_path, 'r') as buisness_file:
        for line in buisness_file.readlines():
            buisness = json.loads(line)

            try:
                id = buisness['business_id']
                price = buisness['attributes']['Price Range']
                prices[id] = price
            except KeyError:
                pass

    return prices


def create_review_to_price(review_dataset_path, buisness_price, output_path):
    with open(review_dataset_path, 'r') as review_file:
        with open(output_path, 'w') as out_file:

            lines = review_file.readlines()

            print('Found {} reviews'.format(len(lines)))

            for index, line in enumerate(lines):

                if index % (len(lines) // 100) == 0:
                    progress_bar(index // (len(lines) // 100))

                review = json.loads(line)
                target_id = review['business_id']

                try:
                    out_file.write(json.dumps({'price': buisness_price[target_id],
                                               'text': [sentence.split() for sentence in
                                                        sent_tokenize(review['text'])]
                                               }) + '\n')

                except KeyError:
                    pass


def progress_bar(progress):
    sys.stdout.write('\r[{0}] {1}%'.format('#' * progress + ' ' * (100 - progress), progress))
    sys.stdout.flush()


def main():
    review_path = sys.argv[1]
    business_path = sys.argv[2]
    out_path = sys.argv[3]

    buisness_prices = business_id_to_price(business_path)
    create_review_to_price(review_path, buisness_prices, out_path)


if __name__ == '__main__':
    main()

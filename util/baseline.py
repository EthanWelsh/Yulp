from util.parse_reviews import retrieve_reviews

if __name__ == '__main__':
    reviews = retrieve_reviews(5000, data_path='../data/reviews.json')

    dollar_counts = {}

    _, labels = zip(*reviews)

    for label in labels:
        dollar_counts[label] = dollar_counts.get(label, 0) + 1

    print(dollar_counts)

    print('0: {:.2%}'.format(2517/5000))
    print('1: {:.2%}'.format((1752 + 666) / 5000))
    print('2: {:.2%}'.format(93/5000))


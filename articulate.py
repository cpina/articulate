import random

LIST_OF_WORDS = 'data/english/words.csv'
EXCLUSION = 'data/english/excluded.csv'


def random_word():
    list_of_words = open(LIST_OF_WORDS).read().split('\n')
    exclusion = open(EXCLUSION).read().split('\n')

    while True:
        word = random.choice(list_of_words)

        if word not in exclusion:
            return word


def main():
    while True:
        print(random_word())

if __name__ == '__main__':
    main()
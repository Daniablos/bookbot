import sys
from stats import *
def get_book_text(filepath):

    with open(filepath) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print('Found', count_words(get_book_text(sys.argv[1])), "total words")
    print('--------- Character Count -------')
    for i in sort_on(num_characters(get_book_text(sys.argv[1]))):
        if i['char'].isalpha():
            print(i['char']+':', i['num'])
    print('============= END ===============')
        

main()
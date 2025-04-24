import sys

from .stats import count_characters, count_words, print_sorted_characters


def get_book_text(filepath: str) -> str:
    content: str
    with open(filepath) as f:
        content = f.read()

    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    print("BOOKBOT".center(50, "="))
    print("Analyzing book found at", sys.argv[1])
    print("Word Count".center(50, "="))
    print("Found", count_words(text), "total words")
    print("Character Count".center(50, "="))
    print_sorted_characters(count_characters(text))
    print("END".center(50, "="))


if __name__ == "__main__":
    main()

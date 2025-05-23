import argparse

from .stats import count_characters, count_words, print_sorted_characters

# Return content of file
def get_book_text(filepath: str) -> str:
    content: str
    with open(filepath) as f:
        content = f.read()

    return content


def main():
    parser = argparse.ArgumentParser(description="Подсчёт статистики текста.")
    parser.add_argument("filepath", type=str, help="Путь к файлу книги (например, books/frankenstein.txt)")
    parser.add_argument("--words", action="store_true", help="Вывести количество слов")
    args = parser.parse_args()

    text = get_book_text(args.filepath)
    num_words = count_words(text)

    if args.words:
        print(num_words) 
    else:
        print("BOOKBOT".center(50, "="))
        print("Analyzing book found at", args.filepath)
        print("Word Count".center(50, "="))
        print("Found", num_words, "total words")
        print("Character Count".center(50, "="))
        print_sorted_characters(count_characters(text))
        print("END".center(50, "="))


if __name__ == "__main__":
    main()

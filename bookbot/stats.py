from collections import Counter

# Return number of words
def count_words(content: str) -> int:
    return len(str.split(content))

# Return number of each character
def count_characters(content: str) -> dict[str, int]:
    return Counter(c for c in content.lower() if c.isalpha())

# Sorts by quantity and print dict of characters
def print_sorted_characters(dict_chars: dict[str, int]):
    for key, value in sorted(dict_chars.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")

    pass

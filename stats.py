from collections import Counter

def count_words(content: str):
    return len(str.split(content))

def num_characters(content: str):
    return Counter(c for c in content.lower() if c.isalpha())

def print_sorted_characters(dict_chars: dict):
    for key, value in sorted(dict_chars.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {value}")
    
    pass
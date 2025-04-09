def count_words(content):
    return len(str.split(content))

def num_characters(content):

    lower_content = str.lower(content)
    dict_chars = {}

    for chars in lower_content:
        if chars.isalpha():
            dict_chars[chars] = dict_chars.get(chars, 0) + 1


    return dict_chars


def sort_on(dict_chars: dict):
    list_dict = [{"char": k, "num": v} for k, v in dict_chars.items()]
    list_dict.sort(key=lambda x: x['num'], reverse=True)    
    
    return list_dict
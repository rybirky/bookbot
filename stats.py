def words_in_book(text):
    words = text.split()
    return len(words)

def num_characters(text):
    char_num = {}
    text = text.lower()
    for char in text:
        if char not in char_num:
            char_num[char] = 1
        else:
            char_num[char] += 1
    return char_num

def by_num(char_num):
    return char_num["num"]

def sort_dict(char_num):
    sorted_dict = []
    for char, count in char_num.items():
        sorted_dict.append({"char": char, "num": count})
    sorted_dict.sort(reverse=True, key=by_num)
    return sorted_dict

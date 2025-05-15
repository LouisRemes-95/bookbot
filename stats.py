def get_num_words(text):
    return len(text.split())

def get_num_char(text):
    num_char = {}
    for char in text.lower():
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def sort_char(num_char):
    sorted_char = []
    for key, value in num_char.items():
        sorted_char.append({"char": key, "num": value})
    sorted_char.sort(reverse=True, key = lambda dict: dict["num"])
    return sorted_char

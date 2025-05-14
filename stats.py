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


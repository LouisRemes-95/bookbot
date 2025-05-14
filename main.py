from stats import get_num_words, get_num_char

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{get_num_words(text)} words found in the document")
    for key, value in get_num_char(text).items():
        print(f"'{key}': {value}")

main()
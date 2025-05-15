from stats import get_num_words, get_num_char, sort_char

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    for char in sort_char(get_num_char(text)):
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

main()
from stats import get_num_words, get_num_char, sort_char
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        text = get_book_text(sys.argv[1])

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")

        for char in sort_char(get_num_char(text)):
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")

        print("============= END ===============")

main()
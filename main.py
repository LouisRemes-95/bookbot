def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{count_words(text)} words found in the document")

main()
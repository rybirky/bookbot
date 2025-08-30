import sys
from stats import words_in_book, num_characters, by_num, sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = (sys.argv[1])
    text = get_books_text(book_path)
    num_words = words_in_book(text)
    char_count = num_characters(text)
    sorted_dict = sort_dict(char_count)
    print(f"Analyzing book found at {book_path}")
    print(f"Found {num_words} total words")
    for item in sorted_dict:
        ch = item["char"]
        cnt = item["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")

def get_books_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
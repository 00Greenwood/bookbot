from stats import get_num_words, get_freq_chars, get_sorted_chars
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_book_file_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    print("============ BOOKBOT ============")
    book_file_path = get_book_file_path()
    file_path = f"./{book_file_path}"
    print(f"Analyzing book found at {file_path}...")
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    freq_chars = get_freq_chars(book_text)
    sorted_chars = get_sorted_chars(freq_chars)
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()

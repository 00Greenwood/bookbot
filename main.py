from stats import get_num_words, get_freq_chars, get_sorted_chars


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    file_path = "./books/frankenstein.txt"
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

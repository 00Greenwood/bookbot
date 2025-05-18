def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")


main()

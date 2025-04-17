def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def get_num_words():
    num_words_list = text.split()
    num_words = len(num_words_list)
    return num_words

def main():
    path = "books/frankenstein.txt"
    get_book_text(path)
    get_num_words(text)
    print(f"{num_words} words found in the document")
    
main()

"""
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()
"""
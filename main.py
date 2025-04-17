from stats import get_num_words, count_chars

# GETS ALL THE TEXT FROM A FILE, AS LONG AS THE PATH IS SUPPLIED
def get_book_text(path):
    with open(path) as f:
        return f.read()

# SAVES THE TEXT OF THE FRANKENSTEIN BOOK ON THE FULL_TEXT VARIABLE
# SAVES THE RESULT OF THE WORD COUNT OF FULL_TEXT VARIABLE ON THE TOTAL_WORDS VARIABLE
def main():
    full_text = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(full_text)
    final = count_chars(full_text)
    print(f"{total_words} words found in the document")
    print(final)

main()
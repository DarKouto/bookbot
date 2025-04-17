from stats import get_num_words, count_chars

# GETS ALL THE TEXT FROM A FILE, AS LONG AS THE PATH IS SUPPLIED
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # CAPTURES THE RETURN OF THE get_book_text FUNCTION ON THE FULL_BOOK VARIABLE
    full_book = get_book_text("books/frankenstein.txt")
    
    # CAPTURES THE RETURN OF THE get_num_words FUNCTION ON THE TOTAL_WORDS VARIABLE
    total_words = get_num_words(full_book)
    print(f"{total_words} words found in the document")

    # CAPTURES THE RETURN of the count_chars FUNCTION ON THE CHAR_COUNT VARIABLE
    char_count = count_chars(full_book)
    print(char_count)

main()
import sys # IMPORTS A SYSTEM MODULE, TO ACCESS FILE PATHS AND SUCH
from stats import get_num_words, count_chars, sort_chars



# GETS ALL THE TEXT FROM A FILE, AS LONG AS THE PATH IS SUPPLIED
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    # IF I TYPE PYTHON MAIN.PY, THEN SYS.ARGV = [PYTHON MAIN.PY]
    # IF I TYPE PYTHON MAIN.PY BOOKS/FRANKENSTEIN.TXT, THEN SYS.ARGV = [PYTHON MAIN.PY, BOOKS/FRANKENSTEIN.TXT]
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # THIS MEANS THAT THE INDEX 1 OF sys.argv
    path_to_book = sys.argv[1]


    # CAPTURES THE RETURN OF THE get_book_text FUNCTION ON THE FULL_BOOK VARIABLE
    full_book = get_book_text(path_to_book)
    
    # CAPTURES THE RETURN OF THE get_num_words FUNCTION ON THE TOTAL_WORDS VARIABLE
    total_words = get_num_words(full_book)
    
    # CAPTURES THE RETURN of the count_chars FUNCTION ON THE CHAR_COUNT VARIABLE
    char_count = count_chars(full_book)

    #CAPURES THE RETURN OF THE sort_chars FUNCTION ON THE SORTED_CHARS VARIABLE
    sorted_chars = sort_chars(char_count)
    
    # PRINTS
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha() == True:
            character = char_dict["char"]  
            count = char_dict["count"]
            print(f"{character}: {count}")

    print("============= END ===============")

main()
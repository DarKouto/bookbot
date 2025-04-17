# GETS ALL THE TEXT FROM A FILE, AS LONG AS THE PATH IS SUPPLIED
def get_book_text(path):
    with open(path) as f:
        return f.read()

# USES THE SPLIT METHOD ON THE STRING, WHICH SAVES EACH WORD AS AN ITEM ON A LIST
# SO IF WE GET THE LENGHT OF THAT ARRAY, WE GET THE NUMBER OF WORDS   
def get_num_words(text):
    num_words_list = text.split()
    num_words = len(num_words_list)
    return num_words

# SAVES THE TEXT OF THE FRANKENSTEIN BOOK ON THE FULL_TEXT VARIABLE
# SAVES THE RESULT OF THE WORD COUNT OF FULL_TEXT VARIABLE ON THE TOTAL_WORDS VARIABLE
def main():
    full_text = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(full_text)
    print(f"{total_words} words found in the document")

main()
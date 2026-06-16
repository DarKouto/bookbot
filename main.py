from stats import get_num_words, count_chars, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    
    path_to_book = "books/frankenstein.txt"
    full_book = get_book_text(path_to_book)
    total_words = get_num_words(full_book)
    char_count = count_chars(full_book)
    sorted_list = chars_dict_to_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_list:
        if char.isalpha() == True:
            new_tpl=(char,count)
            print(new_tpl)

    print("============= END ===============")

main()
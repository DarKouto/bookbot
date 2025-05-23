# USES THE SPLIT METHOD ON THE STRING, WHICH SAVES EACH WORD AS AN ITEM ON A LIST
# SO IF WE GET THE LENGHT OF THAT LIST, WE GET THE NUMBER OF WORDS   
def get_num_words(text):
    num_words_list = text.split()
    num_words = len(num_words_list)
    return num_words

# CONVERTS ALL CHARS TO LOWER CASE
# ADDS THEM TO THE DICT IF NOT FOUND WITH THE VALUE OF 1
# INCREMENTS +1 IF THE KEY IS ALREADY THERE
def count_chars(text):
    text_lower = text.lower()
    count_dict = {}
    for char in text_lower:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

# TAKES THE CHAR:COUNT DICITIONARY AS AN ARGUMENT
# CONVERTS IT TO A LIST, BECAUSE SORT() CAN ONLY BE USED ON LISTS
# THE LIST CONTAINS SEVERAL DICTIONARIES, ONE FOR EACH CHARACTER WITH COUNTS
def sort_chars(dict):
    sorted_list = []

    for char, count in dict.items():
        sorted_list.append({"char": char, "count": count})
    
    def sorting_key(dict2):
        return dict2["count"]

    sorted_list.sort(reverse=True, key=sorting_key)
    return sorted_list
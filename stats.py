def get_num_words(text):
    num_words_list = text.split()
    num_words = len(num_words_list)
    return num_words

def count_chars(text):
    text_lower = text.lower()
    count_dict = {}
    for char in text_lower:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def sort_chars(dict):
    sorted_list = []
    for char, count in dict.items():
        sorted_list.append({"char": char, "count": count})
    
    def sorting_key(dict2):
        return dict2["count"]
    
    sorted_list.sort(reverse=True, key=sorting_key)
    return sorted_list

def sort_on(tpl):
    return (tpl[1])

def chars_dict_to_sorted_list(count_dict):
    new_list = []
    for char, count in count_dict.items():
        new_list.append((char,count))
    return sorted(new_list, key=sort_on, reverse=True)
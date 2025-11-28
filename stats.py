import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def get_num_words(file_content):
    splited = file_content.split()
    num_words = 0
    for i in splited:
        num_words += 1
    return num_words
    
def get_word_count(file_content):
    splited = file_content.split()
    count_dict = {}
    for word in splited:
        word = word.lower()
        for letter in word:
            if letter not in count_dict:
                count_dict[letter] = 1
            else:
                count_dict[letter] += 1
    return count_dict

def sort(dic, num_words, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_dicts = []
    for key in dic:
        diction = {"name":key,"num":dic[key]}
        list_of_dicts.append(diction)
        list_of_dicts.sort(key=lambda d: d["num"], reverse=True)
    for item in list_of_dicts:
        print(f"{item['name']}: {item['num']}")
    print("============= END ===============")

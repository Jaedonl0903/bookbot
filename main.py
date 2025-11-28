from stats import get_num_words
from stats import get_book_text
from stats import get_word_count
from stats import sort  

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file_content = get_book_text(sys.argv[1])
    num_words = get_num_words(file_content)
    dic = get_word_count(file_content)
    sort(dic,num_words,sys.argv[1])
    
    
main()
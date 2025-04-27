from stats import *
import string
import sys

def get_book_text(src):
    with open(src) as f:
        file_contents = f.read()
    
    return file_contents


def main(): 
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    #path = './books/frankenstein.txt'
    file=get_book_text(path)
    value = numbers_of_characters(file)
    print (f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")

    print(f"Found {count_words(file)} total words")

    print("--------- Character Count -------")

    for x in number_of_alfachars(value):
        if x["char"].isalpha():
            print (f"{x['char']}: {x['num']}")

    print("============= END ===============")
main()
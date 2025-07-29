import sys

from stats import count_words
from stats import count_appereances
from stats import sort_dictionary

def get_book_bot(path):
    with open(path) as f:
        file_content = f.read()
    
    return file_content

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
         
    path = sys.argv[1]
    text = get_book_bot(path)
    word_count = count_words(text)
#    print(f"{word_count} words found in the document")
    appereances = {}
    appereances = count_appereances(text)
    sorted_appereances = []
    sorted_appereances = sort_dictionary(appereances)
#    print(appereances)
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {path}...")
    print(f"----------- Word Count ---------- \nFound {word_count} total words")
    print(f"--------- Character Count -------")
    for i in sorted_appereances:
            print(f"{i['char']}: {i['num']}")
    print(f"============= END ===============")
main()
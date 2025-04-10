
# from <python file> import <function>
import sys
from stats import (
    get_book_text,
    book_word_count,
    get_letter_count,
    write_book_report
)

if(len(sys.argv) != 2):
    print("Incorrect call to bookbot!")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

#------------------------------
#------------------------------
def main():
    book = get_book_text(file_path)
    #print(book)

    count = book_word_count(file_path)
    #print(f"{count} words found in the document")

    letters = get_letter_count(file_path)
    #print(letters)

    write_book_report(file_path)

#------------------------------
#------------------------------
main()
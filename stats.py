
#------------------------------
#------------------------------
def get_book_text(file_path):

    with open(file_path) as f:
        book_text = f.read()

    return book_text

#------------------------------
#------------------------------
def book_word_count(file_path):
    book_text = get_book_text(file_path)
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count


#------------------------------
#------------------------------
def get_letter_count(file_path):
    book_text = get_book_text(file_path)

    char_record = {}

    for char in book_text:
        char = char.lower()

        if(char not in char_record):
            char_record[char] = 1
        else:
            char_record[char] += 1

    return char_record

#------------------------------
#------------------------------
def sort_on(d):
    return d["num"]

#------------------------------
#------------------------------
def write_book_report(file_path):
    count = book_word_count(file_path)
    letters = get_letter_count(file_path)
    #sort letters dictionary
    sorted_letters = []
    #sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    for ch in letters:
        sorted_letters.append({"char": ch, "num": letters[ch]})
    sorted_letters.sort(reverse=True, key=sort_on)
    #print(sorted_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in sorted_letters:
        if(item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
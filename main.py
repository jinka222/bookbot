def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

from stats import count_characters 

def main():
    # Call the function and capture the returned contents
    book_contents = get_book_text("./books/frankenstein.txt")
    # Count the words in the book
    word_count = count_words(book_contents)
    # Print the result to the console
    print(f"{word_count} words found in the document")
    # Count the characters in the book
    char_count_dict = count_characters(book_contents)
    print(f"Character counts: {char_count_dict}")


if __name__ == "__main__":
    main()



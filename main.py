def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    # Split the text into words and return the count
    words = text.split()
    return len(words)
    
    
def main():
    # Call the function and capture the returned contents
    book_contents = get_book_text("./books/frankenstein.txt")
    # Count the words in the book
    word_count = count_words(book_contents)
    # Print the result to the console
    print(f"{word_count} words found in the document")

main()



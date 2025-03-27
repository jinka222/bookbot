def count_words(text):
    # Split the text into words and return the count
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If it's the first time the character is encountered, add it to the dictionary
            char_count[char] = 1
    
    return char_count
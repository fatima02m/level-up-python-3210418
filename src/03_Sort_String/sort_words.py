def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))
# words.split() splits the words at the spaces and gives a list
# key=str.casefold, tells the sorted() method to ignore the case of the words
#sorted() sorts the list of words alphabetically
#.join puts the words list back into a string

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE

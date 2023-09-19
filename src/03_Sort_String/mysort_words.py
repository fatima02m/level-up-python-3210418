# sorts words in a string alphabetically

import string


def sort_string(str):
    # splits the string into words
    list = str.split()
    # sorts them alphabetically using built in function sorted
    sorted_str = sorted(list)
    return sorted_str


if __name__ == '__main__':
    print(sort_string('banana APPLE carrot watermelon peach'))

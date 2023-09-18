from collections import deque
import string
#strategy:
  #remove spaces and punctuation
def palindrome(word):
    
    #removes punctuations
    word = word.translate(str.maketrans('', '', string.punctuation))
    #removes whitespaces
    d = deque(''.join(word.split()))
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


if __name__ == '__main__':
    print(palindrome("go hang a salami - i'm a lasagna hog"))
    print(palindrome("fatima"))

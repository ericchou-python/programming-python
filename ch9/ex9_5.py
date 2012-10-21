#!/usr/bin/env python

# Needed to look at the answer
# Reverse the logic as in 9.4

def uses_only(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

input_word = raw_input("Enter a word: ")
input_letters = raw_input("Enter a string of letters: ")

result = uses_only(input_word, input_letters)
print result

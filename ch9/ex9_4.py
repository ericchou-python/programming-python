#!/usr/bin/env python

# Needed to look at the answer
# The blind spot was the reverse logic

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

input_word = raw_input("Enter a word: ")
input_letters = raw_input("Enter a string of letters: ")

result = uses_only(input_word, input_letters)
print result

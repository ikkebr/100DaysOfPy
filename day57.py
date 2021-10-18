#!/usr/bin/env python3

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.


def reverse_words(s: str) -> str:
    list_of_words = s.split(" ")
    return " ".join(reversed([x for x in list_of_words if x]))


print(reverse_words("the sky is blue"))  # prints "blue is sky the"
print(reverse_words("a good   example"))  # prints "example good a"
print(reverse_words("  Bob    Loves  Alice   "))  # prints "Alice Loves Bob"

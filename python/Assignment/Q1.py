# Problem Statement: Letter Combinations of a Phone Number

# You are given a string digits consisting of numeric characters from 2 to 9 only. 
# Each digit maps to a set of letters as found on a traditional telephone keypad.
# Your task is to generate all possible letter combinations that the given digit string can represent.

# Telephone Keypad Mapping
# Digit     Letters
# 2         a b c
# 3         d e f
# 4         g h i
# 5         j k l
# 6         m n o
# 7         p q r s
# 8         t u v
# 9         w x y z

# Note:
# Digit 1 does not map to any letters. The output combinations can be returned in any order

############################################################################################################
# Input
# A string digits of length between 1 and 4. 
# Each character in digits is between '2' and '9'
#
# Output
# A list of all possible letter combinations formed by 
# replacing each digit with its corresponding letters
###########################################################################################################
###### Examples ######
# Example 1
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2
# Input: digits = "2"
# Output: ["a","b","c"]

# Task
# Write a program/function to generate and return all valid letter combinations for the given digit string.

dict = {
    '1' : [],
    '2' : ['a', 'b', 'c'],
    '3' : ['d', 'e', 'f'],
    '4' : ['g', 'h', 'i'],
    '5' : ['j', 'k', 'l'],
    '6' : ['m', 'n', 'o'],
    '7' : ['p', 'q', 'r', 's'],
    '8' : ['t', 'u', 'v'],
    '9' : ['w', 'x', 'y', 'z'],
}
def keyPad(digits, ps=[]):
    nps = []
    if ps:
        for letter in dict.get(digits[-1]):
            for item in ps:
                nps.append(letter+item)
    else:
        nps = dict.get(digits[-1])
        
    return keyPad(digits[:-1], nps) if len(digits) > 1 else nps

print(keyPad("23"))
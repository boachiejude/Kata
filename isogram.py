"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram.
Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

def is_isogram(string):
    interpreted = string.lower()                # Converts the string argument to lowercase
    for char in interpreted:
        if interpreted.count(char) > 1:         # If .count() finds more than one occurence of the character, the function returns False
            return False
    return True                                 # After going through all the characters and not finding duplicates, the funtion returns True

# Testing
# The code below is not included in the code I submitted on codewars

testwords = ["Dermatoglyphics", "aba", "moOse", "isIsogram"] 
for i in testwords:
    print(is_isogram(i))
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_words(string: str)->str:
    string = string.split("-")
    string.sort()
    return "-".join(string)

print(sort_words("green-red-yellow-black-white"))
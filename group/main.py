# Write a Python function to check whether a string is a pangram or not.
# # Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# # For example : "The quick brown fox jumps over the lazy dog"


def is_pangram(string: str)->bool:
    string = string.lower()
    for char in "abcdefghijklmnopqrstvwxz":
        if char not in string:
            return False
    return True

print(is_pangram("dog"))

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# str = 'The quick brown fox jumps over teh lazy dog'

# def pangram(str, alphabet):
#     flag = True
#     for char in alphabet:
#         if char not in str.lower():
#             flag = False
            
#     if(flag == True):
#         print("Str is a pangram")
        
#     else:
#         print('Str is not a pangram')
        
# pangram(str, alphabet)


# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_words(string: str)->str:
    string = string.split("-")
    string.sort()
    return "-".join(string)

print(sort_words("green-red-yellow-black-white"))



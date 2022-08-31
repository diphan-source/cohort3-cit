
# write a program that converts minutes to seconds 
from distutils.filelist import translate_pattern


def convert_min_to_sec(min:int)->int:
    return min*60

print(convert_min_to_sec(5))

# write a program to calculate the area of a triangle
def area_of_triangle(base:int , height:int)->int:
    return (base*height)/2

print(area_of_triangle(2, 3))

# 3. Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_even_odd(num : list)->list:
   if not isinstance(num , list):
       raise "invalid input"
   
   sum_even = 0
   sum_odd = 0
   for i in num:
       if i % 2 == 0:
           sum_even += i
       else:
           sum_odd += i
   return[sum_even , sum_odd]
       
print(sum_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# in  cricket , an over consists of six deliveries a bowler bowls from one end
# create a function that takes the number of balls bowled by a bowler 
# calculate the number of overs bowled by the bowler return the value as a float , in the format overs.balls

def overs_bowled(balls:int)->float:
    if not isinstance(balls , int):
        raise "invalid input"
    return balls/6

print(overs_bowled(120))

# 5. create a function that takes two numbers as argumnets (num , length)
# return a list of multiples of num up to length

def multiples_of_num(num:int , length:int)->list:
    if not isinstance(num , int) or not isinstance(length , int):
        raise "invalid input"
    return [num*i for i in range(1, length + 1)]

print(multiples_of_num(2, 10))

# 6.Given a list of words in a singular form 
# return a set of those words in plural form if they appear more than once in the list

def pluralize(words:list)->set:
    if not isinstance(words , list):
        raise "invalid input"
    return set([i + 's' for i in words if words.count(i) > 1])

print(pluralize(['cow', 'pig', 'cow', 'cow']))

# create a function thats a dictionary like objects { "name": "John", "notes": [3, 5, 4]} 
# return a dictionary like objects { "name": "John", "top_note": 5}

def top_note_student(dictionary:dict)->dict:
    if not isinstance(dictionary , dict):
        raise "invalid input"
    
    for key , value in dictionary.items():
        if isinstance(value , list):
            dictionary[key] = max(value)
    dictionary['top_note'] = dictionary.pop('notes')
    return dictionary
        
print(top_note_student({"name": "John", "notes": [3, 5, 4]}))

"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
"""

# def encrypt(string:str)->str:
#     if not isinstance(string , str):
#         raise "invalid input"
#     string = string[::-1]
#     string = string.replace('a' , '0')
#     string = string.replace('e' , '1')
#     string = string.replace('i' , '2')
#     string = string.replace('o' , '2')
#     string = string.replace('u' , '3')
#     return string + 'aca'

# print(encrypt('apple'))

def encrypt(string: str)->str:
    if not isinstance(string , str):
        raise TypeError("Exccepted a string as input")
    
    string = string[::-1]
    return string.translate(string.maketrans('aeiou' , '01223')) + 'aca'

print(encrypt('apple'))
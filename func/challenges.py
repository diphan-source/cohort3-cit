
# write a program that converts minutes to seconds 
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

def pluralize(list:list)->set:
    if not isinstance(list , list):
        raise "invalid input"
    return {i + 's' for i in list if list.count(i) > 1}

print(pluralize(['cow', 'pig', 'cow', 'cow']))


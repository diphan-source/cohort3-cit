# 1. Create a 2-D array and slice out the second number in the second column

def _2darray():
    array = [[1, 2], [4, 5], [7, 8]]
    return array[1][1]
print(_2darray())

# 2. Write a python program to sort array element in the ascending/descending order

def _sortarray():
    array =[1, 2, 3, 4, 5, 6, 7, 8, 9]
    array.sort(reverse=True)
    return array
print(_sortarray())

# 3.Write a python program to find the maximum and minimum value in a given 2-D array

def max_min():
    array = [[1, 2], [4, 5]]
    max = array[0][0]
    min = array[0][0]
    for i in range(2):
        for j in range(2):
            if array[i][j] > max:
                max = array[i][j]
            if array[i][j] < min:
                min = array[i][j]
    return f"Max: {max}, Min: {min}"
print(max_min())
"""
4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
percentage less than 50 (Grade C)
percentage equal to 50 and less than 80 (Grade B)
percentage equal to 80 and more than 80 (Grade A)

"""

def _grade(*marks):
    total = 0
    for i in marks:
        total += i
    percentage = (total/500)*100
    if percentage < 50:
        print("Grade C")
    elif percentage == 50 and percentage < 80:
        print("Grade B")
    else:
        print("Grade A")
        
_grade(40,50,70,90,100)

"""
5.Write a python program to fetch only Email ID from text file which include following fields -:
Name
Mobile Number
Roll Number
Email ID

"""

def fetch_email():
    file = open("file.txt", "r")
    for line in file:
        if line.startswith("Email ID"):
            print(line)
            
fetch_email()

"""
6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
 For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”

"""
def check_speed(speed):
    # speed = int(input("Enter the speed: "))
    if speed < 70:
        print("Ok")
    else:
        points = (speed - 70)//5
        if points > 12:
            print("License suspended")
        else:
            print(f"your points are {points}")
            
check_speed(80)
"""
7.Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
"""
def show_stars(rows):
    for i in range(rows):
        print("*" * (i+1))
        
show_stars(5)

"""
8.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
def divisible_7():
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=",")
            
divisible_7()

"""
9.Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. 
Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
def _list_tuple():
    numbers = input("Enter the numbers: ")
    list = numbers.split(",")
    tuple = tuple(list)
    return list, tuple

print(_list_tuple())

"""
10.Write a program that calculates and prints the value according to the given formula: 
Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. 
D is the variable whose values should be input to your program in a comma-separated sequence. 
Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
The output of the program should be: 18,22,24
"""
def _formula():
    D = input("Enter the values: ")
    C = 50
    H = 30
    Q = []
    for i in D:
        Q.append((2 * C * i)/H)
    return Q
print(_formula())

"""
11.Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
def func_compute():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("ZeroDivisionError")
        
func_compute()

"""
12.Create a nesting list that prints out the color and the car brand.
"""
def nesting_list():
    colors = ["red", "blue", "green"]
    cars = ["BMW", "Audi", "Toyota"]
    for i in colors:
        for j in cars:
            print(i, j)
            
nesting_list()
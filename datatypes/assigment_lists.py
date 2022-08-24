"""1. Write a Python program to sum all the items in a list.
    - The list should be generated using list comprehension
    - The size of the list should be from a user input

2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`

3. Write a Python program to remove duplicates from a list, given list
    `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

5. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
"""

if __name__ == "__main__":
    menu = """
Assigment for Cit class 24/08/2022
1. Sum all the items in a list.
2. count the number of strings 
3. remove duplicates from a list
4. print a specified list after removing the 0th, 4th and 5th elements.
5. generate and print a list except for the first 5 elements
"""
print(menu)
choice = 0 
choice = int(input("Enter your choice: "))
if choice == 1:
    """ 
    Sum all the items in a list.
    The list should be generated using list comprehension
    The size of the list should be from a user input
    """ 
    print("========List & sum of the list items========")
    size = int(input("Enter the size of the list: "))
    my_list = [x for x in range(size)]
    print(my_list)
    print(sum(my_list))
elif choice == 2:
    """
    Write a Python program to count the number of strings where the string 
    length is 2 or more and the first and last character are same from a given list of strings. 
    Sample List : `['abc', 'xyz', 'aba', '1221']`
    """
    print("========Count the number of strings========")
    sample_list = ["abc", "xyz", "aba", "1221"]
    count = 0
    for i in sample_list:
       if len(i) > 2 and i[0] == i[-1]:
        count = count + 1
    print(f"The number of strings is {count}")
elif choice == 3:
    """
    Write a Python program to remove duplicates from a list, given list
    fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
    """
    print("========Remove duplicates from a list========")
    fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
    print(fruits)
    print(list(set(fruits)))
    
elif choice == 4:
    
    """
    Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : 
    `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`
    """
    print("========Print a specified list after removing the 0th, 4th and 5th elements========")
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    specified_list = sample_list[1:4]
    print(sample_list)
    print(specified_list)
elif choice == 5:
    """
    Write a Python program to generate and print a list except for the first 5 elements,
    where the values are square of numbers between 1 and 30 (both included)
    """
    print("========Generate and print a list except for the first 5 elements========")
    sample_list = [x for x in range(1, 31) ]
    square_values = [x ** 2 for x in sample_list]
    print(square_values[5:])
    
else:
    print("Invalid choice")
    exit()
    
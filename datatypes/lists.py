# cars = ["bmw" ,"benz", "jaguar" , "ford" , "apel" , "totyata", ]
# del cars[2:6]
# print(cars)

my_list = ["Apple", "Banana", "Cherry"]

# first item in the list
my_list[0] # Apple

# second item in the list
my_list[1] # Banana

# third item in the list
my_list[2] # Cherry

# last item in the list
my_list[-1] # Cherry

nested_list = ["Apple", ["Banana", "Cherry"], "Durian"]

# first item in the list
nested_list[0] # Apple

# second item in the list
nested_list[1] # ["Banana", "Cherry"]

# first item in the nested list
nested_list[1][0] # Banana

# second item in the nested list
nested_list[1][1] # Cherry



# list slicing
my_list = ["P", "y", "t", "h", "o", "n"]

# elements from index 2 to index 4
my_list[2:5] # ['t', 'h', 'o']

# list slicing
my_list = ["P", "y", "t", "h", "o", "n"]

# elements from index 2 to the end
my_list[2:] # ['t', 'h', 'o', 'n']

# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the value of the first item in the list
odd[0] = 1

print(odd) # [1, 4, 6, 8]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd) # [1, 3, 5, 7, 8]

fruits = ["Apple", "Banana", "Cherry"]

# add one item to the end of the list
fruits.append("Durian")

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian']

# add several items to the end of the list
fruits.extend(["Mango", "Orange"])

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian', 'Mango', 'Orange']

# repeat a list for 3 times
even = [2, 4, 6, 8]

print(even * 3) # [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]

odd = [1, 3, 5, 7]

numbers = even + odd # [2, 4, 6, 8, 1, 3, 5, 7]

fruits = ["Apple", "Banana", "Cherry"]

# insert one item at index 2
fruits.insert(2, "Durian")

print(fruits) # ['Apple', 'Banana', 'Durian', 'Cherry']

# insert multiple items at index 2
fruits.insert(2, ["Mango", "Orange"])

print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Durian', 'Cherry']

# delete one item from a list
fruits = ["Apple", "Banana", "Cherry"]

del fruits[1]

print(fruits) # ['Apple', 'Cherry']

# delete multiple items from a list
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

del fruits[2:4]

print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange']

# delete the list entirely
del fruits

print(fruits) # NameError: name 'fruits' is not defined

fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

# remove the last item
fruits.pop()

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian', 'Mango']

# remove the item at index 2
fruits.pop(2)

print(fruits) # ['Apple', 'Banana', 'Mango']

# empty the list
fruits.clear()

print(fruits) # []
# create a menu with the following options:
# 1. Print First 10 natural numbers using while loop.
# 2. Calculate the sum of all numbers from 1 to a given number.
# 3. Display numbers from -10 to -1 using while loop.
# 4. Count the total number of digits in a number using a while loop.
# 5. Write a program to count the total number of digits in a number using a while loop.
# 6. Write a program to count the total number of digits in a number using a while loop.
# 7. Display numbers from -10 to -1 using while loop.
# 8. Exit

menu = """
1. Print First 10 natural numbers using while loop.
2. Calculate the sum of all numbers from 1 to a given number.
3. Display numbers from -10 to -1 using while loop.
4. Count the total number of digits in a number using a while loop.
5. Write a program to count the total number of digits in a number using a while loop.
6. Write a program to count the total number of digits in a number using a while loop.
7. Display numbers from -10 to -1 using while loop.
8. Exit"""

print(menu)

choice = int(input("Enter your choice: "))

while choice != 8:
    if choice == 1:
        num = 1
        while num <= 10:
            print(num)
            num = num + 1
    elif choice == 2:
        num = 1
        total = 0
        n = int(input("Enter a number: "))
        while num <= n:
            total = total + num
            num = num + 1
        print(total)
    elif choice == 3:
        num = -11
        while num <= -2:
            num = num + 1
            print(num)
    elif choice == 4:
        num = int(input("Enter a number: "))
        counter = 0
        total = 0
        while counter < len(str(num)):
            total = total + 1
            counter = counter + 1
        print(total)
    elif choice == 5:
        num = int(input("Enter a number: "))
        counter = 0
        total = 0
        while counter < len(str(num)):
            total = total + 1
            counter = counter + 1
        print(total)
    elif choice == 6:
        num = int(input("Enter a number: "))
        counter = 0
        total = 0
        while counter < len(str(num)):
            total = total + 1
            counter = counter + 1
        print(total)
    elif choice == 7:
        num = -11
        while num <= -2:
            num = num + 1
            print(num)
    else:
        print("Invalid choice")
    print(menu)
    choice = int(input("Enter your choice: "))
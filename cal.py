# Write a simple calculator that performs operations based on user input

choice = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
if choice == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif choice == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif choice == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif choice == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2)
else:
    print("Invalid choice")
    


"""Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum."""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 * num2 <= 1000:
    print(num1 * num2)
else:
    print(num1 + num2)
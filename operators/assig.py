# Write a program that uses if statement and comparision operators
is_underage = 15
Your_age = int(input("Enter your age: "))
fit_for_marriage =int(input("extended_family or nuclear_family: "))
if fit_for_marriage == 1 and is_underage >= 18:
    print("You are fit for marriage")
else:
    print("You are not fit for marriage")
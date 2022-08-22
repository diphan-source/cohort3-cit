# 3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...

num = int(input("Enter a number: "))
for n in range(1,13):
    print(f"{num} * {n} = {num*n}")

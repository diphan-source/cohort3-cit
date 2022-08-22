# 2. Calculate the sum of all numbers from 1 to a given number.
n = int(input("Enter a number: "))
sum = 0
for n in range(1,n+1):
    print(n)
    sum = sum + n
print(f"Sum of all numbers from 1 to {n} is {sum}")

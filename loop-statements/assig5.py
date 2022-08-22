# 6. Write a program to count the total number of digits in a number using a while loop. given number `4673453`

counter = 0
total = 0
while counter < len(str(4673453)):
    total = total + 1
    counter = counter + 1
print(total)
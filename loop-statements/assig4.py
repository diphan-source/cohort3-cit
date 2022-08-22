""" Write a program to display only those numbers from a list that satisfy the following conditions
   The number must be divisible by five
   If the number is greater than 150, then skip it and move to the next number
   If the number is greater than 500, then stop the loop
   given `numbers = [12, 75, 150, 180, 145, 525, 50]`
   output: `[75, 150, 525]` """
    
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n % 5 == 0:
        if n > 150:
            continue
        if n > 500:
            break
        print(n)
# find the maximum number in a given list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def max_no(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(max_no(list))

max_no(list)

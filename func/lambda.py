
# # normal function 

# def add(x, y):
#     return x + y

# print(add(2, 3))

# # lambda function

# add = lambda x, y: x + y
# print(add(2, 3))

# # example 2
# power = lambda x, y: x ** y
# print(power(2, 3))

# # function 1
# solution = lambda x , y : x + y [x: x in range(1, 10) , y: y in range(1, 10)]
# print(solution(2, 3))

# mulitples of a number till the given range is exhausted 
result = lambda x ,y : [x * i for i in range(1, y + 1)]
print(result(2, 10))

# function 2
lambda_dict = lambda x: {i: i ** 2 for i in x}
print(lambda_dict([1, 2, 3, 4, 5]))


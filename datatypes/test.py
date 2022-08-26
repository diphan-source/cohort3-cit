# car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
# print(car.get("model"))

D = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
D['1'] = 2
print(D[D[D[str(D[1])]]]) 

# D = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'} 
# print(D[D[D[1][2]]], end = " ") 
# print(D[D[1]["A"][2]]) 

nums = list({1: 'One', 2: 'Two'})
print(nums)

# tuple = (1, 2, 3, 4) 
# tuple.append( (5, 6, 7) ) 
# print(len(my_tuple)) 

tuple1 = (1, 2, 4, 3) 
tuple2 = (1, 2, 3, 4) 
print(tuple1 < tuple2) 
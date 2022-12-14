"""
1.Your task is to create slightly different animals, which should have the same properties and methods, 
but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog 
"Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), 
age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food,
remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented
in each animal, as the animals have different sounds.
When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)
"""

class Animal:
    def __init__(self, name, age, food:list ):
        self.__name = name
        self.__age = age
        self.__food = food
        self.talk = self.talk()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    def get_food(self):
        return self.__food

    def add_food(self, food):
        self.__food.append(food)

    def remove_food(self, food):
        self.__food.remove(food)

    def talk(self):
        return f"Hello, I'm {self.__name} "
    
    
class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        
    def talk(self):
        return f"{super().talk()} and I say Moew"
    
class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        
    def talk(self):
        return f"{super().talk()} and I say Woff"
    
class Fish(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        
    def talk(self):
        return f"{super().talk()} and I say Blub"
    
class Cow(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        
    def talk(self):
        return f"{super().talk()} and I say Muuu"
    
list = [Cat("Mittens", 2, ["Milk", "Fish"]), Dog("Rex", 3, ["Meat", "Bones"]), Fish("Nemo", 1, ["Algae"]), Cow("Bessie", 4, ["Grass", "Hay"])]
for animal in list:
    print(animal.talk)
        


"""
2.The snail climbs up 7 feet each day and slips back 2 feet each night. How many days will it take the snail to get out of
a well with the given depth?. Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6

"""
def snail(depth):
    days = 0
    while depth > 0:
        depth -= 7
        days += 1
        if depth > 0:
            depth += 2
    return f"It will take {days} days for the snail to get out of the well."
print(snail(31))

"""
3.Write a function that takes a list of numbers and returns the largest number in the list.

"""

def max_num(list):
    max = 0
    for num in list:
        if num > max:
            max = num
    return max
print(max_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



""""
4.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: Hello world! Then, 
the output should be: UPPER CASE 1 LOWER CASE 9
"""
def upper_lower(sentence):
    upper = 0
    lower = 0
    for letter in sentence:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return f"UPPER CASE {upper} LOWER CASE {lower}"

print(upper_lower("Hello World!"))
# print(upper_lower("Uga M Buga"))



""""
5.Using Object Oriented Programming, write a program that implements a dice game. 
The game should have two players, and each player should have a name and a score. 
The game should have a method called play that takes two players as arguments and simulates the game. 
The game should be played as follows:

Each player rolls a die.
The player with the highest roll wins the round.
The winner gets one point added to their score.
The game ends when one player has 5 points.
The player with the most points at the end of the game wins.
The program should print out the winner's name and score.
If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a 
third time, they get an extra roll, but their turn ends.
"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def play(self, player1, player2):
        while player1.score < 5 and player2.score < 5:
            player1_roll = player1.roll()
            player2_roll = player2.roll()
            if player1_roll > player2_roll:
                player1.score += 1
                print(f"{player1.name} wins the round!")
            elif player2_roll > player1_roll:
                player2.score += 1
                print(f"{player2.name} wins the round!")
            else:
                print("It's a tie!")
        if player1.score > player2.score:
            print(f"{player1.name} wins the game!")
        else:
            print(f"{player2.name} wins the game!")
            
    def roll(self):
        import random
        roll = random.randint(1, 6)
        print(f"{self.name} rolled a {roll}")
        if roll == 6:
            roll += self.roll()
        return roll
    
    def __str__(self):
        return f"{self.name} has {self.score} points."
    
player1 = Player("player", 0)
player2 = Player("player", 0)
player1.play(player1, player2)



""""
6.Write a Python program that lists out all the default as well as custom properties of the class.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(dir(Person))
""""
7.Write a Program in Python to implement a Stack Data Structure using Class and Objects, 
with push, pop, and traversal methods.
"""
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty!")

    def traverse(self):
        print(self.stack)

stack = Stack(5)
for i in range(6):
    stack.push(i)

stack.traverse()
for i in range(6):
    stack.pop()
stack.traverse()


""""
8.Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.
"""

def list_squares(list):
    return [num**2 for num in list]

print(list_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



"""
9.Using only functions and lists, Implement a queue data structure. 
The queue should have the following methods: enqueue, dequeue, and size. 
The queue should be "first-in-first-out" (FIFO).
"""
queue_size = 5
queue = []

def enqueue(item):
    if len(queue) < queue_size:
        queue.append(item)
    else:
        print("Queue is full!")

def dequeue():
    if len(queue) > 0:
        return queue.pop(0)
    else:
        print("Queue is empty!")

def size():
    return len(queue)

for i in range(6):
    enqueue(i)
    print(f"Enqueued {i}")

print(f"Queue size: {size()}")



"""
10.Using a while loop, implement merge sort algorithm.

"""
import random 
def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)
merge_sort(numbers)
print(numbers)
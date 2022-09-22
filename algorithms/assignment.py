"""
1.create a credit card class with the following attributes: card number, expiration date, 
and security code. Create a method that will print out the card number, expiration date, and
security code. Create an instance of the class and call the method.

2.create Animal class and Dog class. 
Make the Dog class inherit from the Animal class. 
Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

3.create a class called Queue. 
The class should have the following methods: enqueue, dequeue, and size. 
The enqueue method should add an item to the queue. 
The dequeue method should remove an item from the queue. 
The size method should return the size of the queue.

4.create a class called Stack. 
The class should have the following methods: push, pop, and size. 
The push method should add an item to the stack. 
The pop method should remove an item from the stack. 
The size method should return the size of the stack.

5.create a class called Person. 
The class should have the following attributes: name, age, and address. 
The class should have the following methods: eat, sleep, and work. 
The eat method should print out the name of the person and the word "is eating". 
The sleep method should print out the name of the person and the word "is sleeping". 
The work method should print out the name of the person and the word "is working".

6.create a class called Employee. 
The class should have the following attributes: name, age, and salary. 
The class should have the following methods: eat, sleep, and work. 
The eat method should print out the name of the person and the word "is eating". 
The sleep method should print out the name of the person and the word "is sleeping". 
The work method should print out the name of the person and the word "is working". 
Create a subclass of Employee called Programmer. 
The Programmer class should have the following attributes: name, age, salary, and programming language. 
The Programmer class should have the following methods: eat, sleep, work, and code. 
The code method should print out the name of the person and the word "is coding in" and the programming language. 
Create an instance of the Programmer class and call all the methods.

7.create a class called Vehicle. 
The class should have the following attributes: make, model, and year. 
The class should have the following methods: start, stop, and drive. 
The start method should print out the make, model, and year of the vehicle and the word "is starting". 
The stop method should print out the make, model, and year of the vehicle and the word "is stopping". 
The drive method should print out the make, model, and year of the vehicle and the word "is driving".
Create a subclass of Vehicle called Car. 
The Car class should have the following attributes: make, model, year, and color.
The Car class should have the following methods: start, stop, drive, and park. 
The park method should print out the make, model, year, and color of the car and the word "is parking". 
Create an instance of the Car class and call all the methods.

8.create a class called Animal. 
The class should have the following attributes: name, color, and age. 
The class should have the following methods: eat, sleep, and make_sound. 
The eat method should print out the name of the animal and the word "is eating". 
The sleep method should print out the name of the animal and the word "is sleeping". 
The make_sound method should print out the name of the animal and the word "is making a sound". 
Create a subclass of Animal called Dog. 
The Dog class should have the following attributes: name, color, age, and breed.
The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
The bark method should print out the name of the dog and the word "is barking". 
Create an instance of the Dog class and call all the methods.

9.create a class of your choice. 
It should have at least 3 attributes and 3 methods where one of the methods is a static method. 
Implement polymorphism, encapsulation, and inheritance.


"""

# solution 1
import datetime
import hashlib
class CreditCard:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%m/%y")
        self.security_code = hashlib.sha256(security_code.encode()).hexdigest()

    def print_card(self):
        print("Card details:")
        print(f"Card number: {self.card_number} \nExpiration date: {self.expiration_date} \nSecurity code: {self.security_code}") 

# instance of the class
visa_card = CreditCard("123456789", "12/21", "1234")
visa_card.print_card()

# solution 2 
class Animal:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

class Dog(Animal):
    def __init__(self, name, color, breed ):
        super().__init__(name, color, breed)

    def bark(self):
        print(f"{self.name} is barking")
        
# instance of the class dog
wild_dog = Dog("Wild Dog", "Brown", "Wild Dog")
wild_dog.bark()

# solution 3
class Queue:
    def __init__(self):
        self.items = []
        self.size = int(input("Enter the size of the queue: "))
        
    def is_empty(self):
        return self.size() == 0
    
    def is_full(self):
        return self.size() == self.size

    def enqueue(self, item):
        if not self.is_full():
            self.items.insert(0, item)
            return True
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    # solution 4
    class stack:
        def __init__(self):
            self.items = []
            self.size = int(input("Enter the size of the stack: "))
            
        def is_empty(self):
            return self.size() == -1
        
        def is_full(self):
            return self.size() == self.size
        
        def push(self, item):
            if not self.is_full():
                self.items.append(item)
                return True
            else:
                print("Stack is full")
                
        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            return None
        
        def size(self):
            return len(self.items)
        
        def __str__(self):
            return str(self.items)
        
#solution 5 
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
    def work(self):
        print(f"{self.name} is working")
        
# example = Person("John", 20, "1234 Main Street")
# example.eat()
# example.sleep()
# example.work()

# solution 6
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
    def work(self):
        print(f"{self.name} is working")
        
class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
        
    def code(self):
        self.programming_language = input("Enter the programming language: ")
        print(f"{self.name} is coding in {self.programming_language}")

# instance of the class Programmer
engineer = Programmer("John", 20, 100000, "Python")
engineer.code()
engineer.eat()
engineer.sleep()
engineer.work()
 
# solution 7
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print(f"{self.make} of {self.model} and {self.year} is starting")
        
    def stop(self):
        print(f"{self.make} of {self.model} and {self.year} is stopping")
        
    def drive(self):
        print(f"{self.make} of {self.model} and {self.year} is driving")
        
class Car(Vehicle):
    def __init__(self, make, model, year ,color):
        super().__init__(make, model, year)
        self.color = color
        
    def park(self):
        print(f"{self.make} of {self.model} , {self.year} and {self.color} is parking")
        
# instance of the class Car
Mercedez = Car("Mercedez", "C200", 2020, "Black")
Mercedez.start()
Mercedez.stop()
Mercedez.drive()
Mercedez.park()

# solution 8
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        
    def make_sound(self):
        print(f"{self.name} is making sound")
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} is barking")
        
# instance of the class Dog
jet = Dog("Jet", "Brown", 2, "German Shepherd")
jet.bark()
jet.eat()
jet.sleep()


# solution 9
class Course:
    def __init__(self, name, duration, price):
        self.name = name
        self.duration = duration
        self.price = price
        self.__department = "Computer Science"
        
        
    def set_department(self, department):
        self.__department = department
        return self.__department
    
    def get_department(self):
        return self.__department
        
    def get_name(self):
        return self.name
    
    def edit_course_name(self, name):
        name = input("Enter the new name of the course: ")
        self.name = name
        return self.name
    
    def get_duration(self):
        return self.duration
    
    @staticmethod
    def edit_course_duration():
        duration = input("Enter the new duration of the course: ")
        print(f"The new duration of the course is {duration} years")
        
    def print_course(self):
        print(f"{self.name} is {self.duration} months and {self.price} dollars")
        
        
class Student(Course):
    def __init__(self, name, duration, price, student_id, student_name):
        super().__init__(name, duration, price)
        self.student_id = student_id
        self.student_name = student_name
        
    def get_student_id(self):
        return self.student_id
    
    def get_student_name(self):
        return self.student_name
    
    def edit_student_name(self, student_name):
        self.name = student_name
        return self.name
    
class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.edit_rights = Course.edit_course_duration()
        
    def print_teacher(self):
        print(f"{self.name} is {self.age} years old and {self.salary} dollars")
        
tech = Teacher("John", 30, 100000)
tech.edit_rights
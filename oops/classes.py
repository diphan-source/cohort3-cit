class Parrot:
    my_attribute = "Hello"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __repr__(self):
        return f"<Parrot {self.name} {self.age} {self.color}>"



# parrot object
parrot = Parrot("parrot", 12, "red")
print(parrot.name)



    
    
    


import string
import random

class Employee:
    def __init__(self, name, salary, age, department):
        self.salary = salary
        self.name = name
        self.age = age
        self.department = department
        self.id = self.create_employee_ID()


    def create_employee_ID(self):
        # EMPYK346
        emp_id = "EMP"
        for _ in range(2):
            emp_id += random.choice(string.ascii_letters)
        for _ in range(3):
            emp_id += random.choice(string.digits)
        return emp_id

    def __repr__(self):
        return f"Name: {self.name} \n Salary: {self.salary} \n Age: {self.age} \
         \n Department: {self.department} \n ID: {self.id}"



employee = Employee("John Doe", 150000.0, 32, "Logistics")
print(employee)






class Animal:
    def __init__(self):
        self.name = "cow"
        self.color = "Brown"

    def change_name(self, name):
        self.name = name

    def print_animal(self):
        print(f"{self.name} {self.color}")


cow = Animal()
print(cow.name)
cow.change_name("Some Cow")
print(cow.name)

class Car:
    def __init__(self, model, color, brand, price):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price

    def move(self, direction, speed):
        print(f"{self.brand} is moving in {direction} direction at a speed of {speed} km/h")

    def stop(self):
        print(f"{self.brand} has stopped")

    def update_price(self, price):
        self.price = price
        print(f"The new price is {self.price}")

import time


car_bmw = Car("X5", "Black", "BMW", 50000.0)
# benz = Car(model, color, brand, price)
# nissan = Car(model, color, brand, price)

print(f"My car is a {car_bmw.color} {car_bmw.model} {car_bmw.brand} that costs {car_bmw.price}")

car_bmw.move("North", 50)
car_bmw.stop()
car_bmw.update_price(600000.00)
print(car_bmw.price)

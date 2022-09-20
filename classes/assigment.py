
# using a class of your choice , implement polymorphism , encapsulation and inheritance


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__role = "Parent"
        
    def setrole(self, role):
        self.__role = role
        
    def get_role(self):
        return self.__role

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        
    def get_school(self):
        return self.school

class length:
    def __init__(self ,x):
        self.x = x
        
    def cent_m(self):
        return self.x * 100
    
class road(length):
    def __init__(self ,x):
        super().__init__(x)
        
    def kilo_m(self):
        return self.x * 1000 
    
    


parent = Parent("John", 45)
print(parent.get_role())
setrole = input("Enter role: ")
print(parent.setrole(setrole))

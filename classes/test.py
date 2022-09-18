

class Animal():
    def __init__(self, name ):
        self.name = name
        self.age = self.determine_age()
        self.breed = self.select_breed()
        
    def determine_age(self):
        age = int(input("Enter age: "))
        if age < 0:
            print("Invalid Age")
        else:
            return age
        
    def select_breed(self):
        breed = input("Enter breed: ")
        if breed == "Dog" or breed == "Cat":
            return breed
        else:
            print("Invalid Breed")
            
class Dog(Animal):
    def __init__(self, name , owner):
        super().__init__(name)
        self.owner = owner
        self.character = 
        
    def __str__(self):
        return f"Name: {self.name} \n Age: {self.age} \n Breed: {self.breed} and Owner: {self.owner}"
    
    
print(Dog("Bingo", "John"))


class customer():
    def __init__(self , name , account_number , balance , type , location):
        super().__init__(name , account_number , balance , type)
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.type = type
        pass
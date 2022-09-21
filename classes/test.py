
class Animal:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed
        
    def __str__(self):
        return f"{self.name} is a {self.breed}"
    
class Dog:
    def __init__(self , bark):
        self.bark = bark
        
    def __str__(self):
        return f"{self.bark}"
    
class Cat:
    def __init__(self , meow):
        self.meow = meow
        
    def __str__(self):
        return f"{self.meow}"
    
class DogCat(Animal , Dog , Cat):
    def __init__(self , name , breed , bark , meow):
        Animal.__init__(self , name , breed)
        Dog.__init__(self , bark)
        Cat.__init__(self , meow)
        
    def __str__(self):
        return f"{self.name} is a {self.breed} and says {self.bark} and {self.meow}"
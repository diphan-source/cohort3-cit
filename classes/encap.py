
class Computer:
    def __init__(self):
        # maxprice is a private attribute to computer class 
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # a method can change the value of a private attribute
    def setMaxPrice(self, price):
        self.__maxprice = price
    # a method can access the value of a private attribute
    def getMaxPrice(self):
        return self.__maxprice
    
    
# encapsulation is the ability to restrict access to methods and variables
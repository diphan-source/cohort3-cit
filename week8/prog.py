"""Write a program that creates a file named answers.txt
 and writes all the answers to the questions in the file.
 The program should then read the file and 
display the contents on the screen."""

class quiz:
    def __init__(self):
        self.file = 'questions.txt'
        self.read_qtns()
        
    
    def write_ans(self, ans):
        with open('answers.txt', 'a') as f:
            f.write(ans + ' \n ')
    
    def read_qtns(self):
        with open(self.file, 'r') as f:
            for line in f:
                print(line)
                ans = input('Enter your answer: ')
                self.write_ans(ans)
        self.read_ans()
                    
    def read_ans(self):
        with open('answers.txt', 'r') as f:
            print('================Answers displayed below from answers.txt================')
            for line in f:
                print(line + '')
                
if __name__ == '__main__':
    quiz = quiz()
            
            












"""1. __init__ method is used to initialize the class attributes
2. __str__ method is used to return a string representation of the object
3. __repr__ method is used to return a string representation of the object
4. __add__ method is used to add two objects
5. __sub__ method is used to subtract two objects
6. __mul__ method is used to multiply two objects
7. __truediv__ method is used to divide two objects
8. __floordiv__ method is used to divide two objects
9. __mod__ method is used to find the remainder of two objects
10. __pow__ method is used to find the power of two objects"""



"""
Interactive quiz Python Project
Create a program that asks the user a series of questions. 
Each question should have a multiple choice answer.
The user should be able to type in the letter of the answer they think is correct. 
After all the questions have been asked,
the program should tell the user how many they got correct and what the correct answers were.

"""

def multiple_choice(question, answer, options):
    print(question)
    correct_ans = 0
    incorrect_ans = 0
    for i in range(len(options)):
        print(options[i])
    while True:
        user_answer = input("Enter your answer: ")
        if user_answer == answer:
            print("Correct!")
            correct_ans += 1
            break
        else:
            print("Incorrect!")
            incorrect_ans += 1
            break
    return correct_ans, incorrect_ans

def main():
    correct_ans = 0
    incorrect_ans = 0
    question1 = "What is the capital of France?"
    answer1 = "a"
    options1 = ["a. Paris", "b. London", "c. Rome", "d. Madrid"]
    question2 = "What is the capital of Spain?"
    answer2 = "d"
    options2 = ["a. Paris", "b. London", "c. Rome", "d. Madrid"]
    question3 = "What is the capital of Italy?"
    answer3 = "c"
    options3 = ["a. Paris", "b. London", "c. Rome", "d. Madrid"]
    question4 = "What is the capital of Germany?"
    answer4 = "b"
    options4 = ["a. Paris", "b. Berlin", "c. Rome", "d. Madrid"]
    question5 = "What is the capital of England?"
    answer5 = "b"
    options5 = ["a. Paris", "b. London", "c. Rome", "d. Madrid"]
    correct_ans += multiple_choice(question1, answer1, options1)[0] + multiple_choice(question2, answer2, options2)[0] + multiple_choice(question3, answer3, options3)[0] + multiple_choice(question4, answer4, options4)[0] + multiple_choice(question5, answer5, options5)[0]
    incorrect_ans += multiple_choice(question1, answer1, options1)[1] + multiple_choice(question2, answer2, options2)[1] + multiple_choice(question3, answer3, options3)[1] + multiple_choice(question4, answer4, options4)[1] + multiple_choice(question5, answer5, options5)[1]
    print("You got", correct_ans, "correct answers and", incorrect_ans, "incorrect answers.")
    
if __name__ == "__main__":
    main()
            


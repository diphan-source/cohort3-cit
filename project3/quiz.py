"""
Interactive quiz Python Project
Create a program that asks the user a series of questions. 
Each question should have a multiple choice answer.
The user should be able to type in the letter of the answer they think is correct. 
After all the questions have been asked,
the program should tell the user how many they got correct and what the correct answers were.

"""

def get_questions():
    questions = []
    with open("questions.txt", "r") as file:
        for line in file:
            questions.append(line.strip().split(","))
    return questions

def get_answers(questions):
    answers = []
    for question in questions:
        print(question[0])
        for i in range(1, len(question)):
            print("{}. {}".format(i, question[i]))
        answer = input("What is your answer? ")
        answers.append(answer)
    return answers

def check_answers(questions, answers):
    score = 0
    for i in range(len(questions)):
        if questions[i][int(answers[i])] == questions[i][1]:
            score =+ 1
    return score 

def main():
    questions = get_questions()
    answers = get_answers(questions)
    score = check_answers(questions, answers)
    print("You got {} correct answers.".format(score))
    
if __name__ == "__main__":
    main()
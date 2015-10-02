import sys
import random
import os

def main():
    fileLocation = getTextFileLocation()
    #QA is a list of length 2 that contains the questions and answers
    QA = readFile(fileLocation)
    questions = QA[0]
    answers = QA[1]

    shuffledQA = getShuffledQuestions(questions, answers)
    shuffledQuestions = shuffledQA[0]
    shuffledAnswers = shuffledQA[1]

    startQuiz(shuffledQuestions, shuffledAnswers)


def getTextFileLocation():
    # Gets the first argument after the name of the program
    if (len(sys.argv) > 1):
        #Argument other than program name provided --> Use Argument
        textFileLocation = sys.argv[1]
        return(textFileLocation)
    else:
        #Only argument provided is the name of the program
        print("\n\nNo Arguments Passed \nProgram Usage: \n   python test.py /location/to/file/\n\n")
        sys.exit()


def readFile(location):
    #Reads the file with the parameters
    questions = []
    answers = []

    print("Location")
    with open(location) as file:
        counter = 1
        for line in file:
            if (line != "\n"):
                if (counter % 2 == 0):
                    #Answers are on the even lines
                    answers.append(line.rstrip("\n"))
                else:
                    #Questions are on the odd lines
                    questions.append(line.rstrip("\n"))

                counter += 1

    return ([questions, answers])


def getShuffledQuestions(questions, answers):
    #Stores the shuffled versions of the questions and answers
    # so that the questions don't always go in the same order
    shuffledQuestions = []
    shuffledAnswers = []

    #indexes = [0, 1, ... len(questions)-1]
    indexes = list(range(len(questions)))
    #shuffle the indexes list
    random.shuffle(indexes)
    #add the shuffled questions / answers by the shuffled indexes
    for index in indexes:
        shuffledQuestions.append(questions[index])
        shuffledAnswers.append(answers[index])

    return([shuffledQuestions, shuffledAnswers])

def startQuiz(questions, answers):
    print(questions)
    print(answers)
    counter = 0
    totalCorrect = 0

    for question in questions:
        os.system('clear')

        counter += 1
        print(str(counter) + ") " + question)
        print(answers[counter-1])

        if (input("Answer: ").lower() == answers[counter-1].lower()):
            totalCorrect += 1
            print("\n Correct!\n Current Score: " + str(totalCorrect) + "/" + str(counter))
            input("\n\n\n\nPress enter to continue...")
        else:
            print("\n Incorrect! The correct answer was: " + answers[counter-1] + "\n Current Score: " + str(totalCorrect) + "/" + str(counter))
            input("\n\n\n\nPress enter to continue...")

    os.system('clear')
    print("\n\n FINAL SCORE: " + str(totalCorrect) + "/" + str(counter))

main()

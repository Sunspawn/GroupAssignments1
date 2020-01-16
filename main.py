"""
Main menu of the project.
"""
from os import path
from Question import Question
from Database import Database
from addImgToDocx import addImgToDocx
data = {}
if path.isfile("database.json"):
    data = Database.readData()

while(True):
    option = input("\nEnter what you want to do:\nAdd a question - 1\nShow all questions - 2\nAdd to image to word file - 3\nExit the program - 4\n")
    if option == '1':
        question = Question(12314,"asd","aaa","topic","subject",True,"FULL")
        data[question.serial] = question.__dict__()
        question = Question(52231,"ASD","AAA","TOPIC","SUBJECT",True,"HALF")
        data[question.serial] = question.__dict__()
    elif option == '2':
        if len(data) == 0:
            print("The database is empty, add questions first.\n")
        else:
            questNum = 1
            for question in data.values():
                print("Question number: " + str(questNum))
                print(question)
                questNum += 1
    elif option == '3':
        addImgToDocx()
    elif option == '4':
        print("Good Bye\n")
        exit(1)

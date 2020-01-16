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
print()
print(type(data))
while(True):
    option = input("Enter what you want to do:\nAdd a question - 1\nShow all questions - 2\nAdd to image to word file - 3\n")
    if option == '1':
        question = Question(12314,"asd","aaa","topic","subject","A",True,"Full")
        print(question.__str__())
        data[question.serial] = question
    elif option == '2':
        print(data)
    elif option == '3':
        addImgToDocx()

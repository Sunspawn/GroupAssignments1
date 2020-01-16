from PermissionKey import PermissionKey
from Course import Course
from Test import Test
from Question import Question
import json


class Database:
    """The database.
:field courses: A list of the courses in the database.
:field tests: A list of the tests in the database.
:field questions: A list of the individual questions in the database.
"""
    def __init__(self):
        self.courses = {}
        self.tests = {}
        self.questions = {}

    def add_course(self, course, permission):
        if (type(permission) is not PermissionKey) or (not permission.access_questions):
            return False
        if type(course) is not Course:
            return False
        # If it's not already in, add it.
        if course.serial not in self.courses.keys():
            self.courses[course.serial] = course
            # Now add the tests for this course.
            for t in course.tests.values():
                self.add_test(t, permission)
            return True
        return False

    def add_test(self, test, permission):
        if (type(permission) is not PermissionKey) or (not permission.access_questions):
            return False
        if type(test) is not Test:
            return False
        if test.serial not in self.tests.keys():
            self.tests[test.serial] = test
            # for each test, add the new questions.
            for q in test.questions.values():
                self.add_question(q, permission)
        return True

    def add_question(self, question, permission):
        if (type(permission) is not PermissionKey) or (not permission.access_questions):
            return False
        if type(question) is not Question:
            return False
        if question.serial not in self.questions.keys():
            self.questions[question.serial] = question
            return True
        return False

    def writeData(obj):
        with open("database.json", "w") as writeToFile:
            json.dump(obj, writeToFile)

    def readData():
        with open("database.json", "r") as readFromFile:
            dict = json.load(readFromFile)
            return dict


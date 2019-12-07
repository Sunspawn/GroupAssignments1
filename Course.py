class Course:
    """
:field serial: The serial number of the course in the database.
:field name: The name of the course.
:field tests: A list of the tests in the course's history.
"""
    def __init__(self, serial, name, tests=[]):
        self.serial = serial
        self.name = name
        self.tests = tests

    def add_test(self, test):
        self.tests.append(test)

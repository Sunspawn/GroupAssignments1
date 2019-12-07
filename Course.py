class Course:
    """
:field serial: The serial number of the course in the database.
:field course_name: The name of the course.
:field proffesor_name: the name of the proffesor.
:field tests: A list of the tests in the course's history.
"""
    def __init__(self, serial, course_name, proffesor_name, tests=[]):
        self.serial = serial
        self.course_name = course_name
        self.proffesor_name = proffesor_name
        self.tests = tests

    def add_test(self, test):
        self.tests.append(test)

from Test import Test


class Course:
    """
:field serial: The serial number of the course in the database.
:field name: The name of the course.
:field tests: A list of the tests in the course's history.
"""
    def __init__(self, serial, name, tests={}):
        for t in tests:
            if type(t) is not Test:
                raise TypeError('Non-Test argument in tests.')
        self.serial = serial
        self.name = name
        self.tests = dict.copy(tests)

    def add_test(self, test):
        if type(test) is not Test:
            return False
        if test.serial not in self.tests.keys():
            self.tests[test.serial] = test
            return True
        return False

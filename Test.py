from Question import Question


class Test:
    """Test class.
:field serial: The serial number in the database.
:field year: The year of the test.
:field semester: The semester the test was taken.
:field specific_date: First, second or the special date.
:field course: The serial number of the course the test is for.
:field maker: The lecturer who wrote the test.
:field questions: A list of the questions in the test.
"""
    def __init__(self, serial, year, semester, specific_date, course, maker, questions={}):
        for q in questions:
            if type(q) is not Question:
                raise TypeError('A non-Question argument in questions.')
        self.serial = serial
        self.year = year
        self.semester = semester
        self.specific_date = specific_date
        self.course = course
        self.maker = str(maker)
        self.questions = dict.copy(questions)

    def add_question(self, question):
        if type(question) is not Question:
            return False
        if question.serial not in self.questions.keys():
            self.questions[question.serial] = question
            return True
        return False

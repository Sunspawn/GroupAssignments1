class Test:
    """Test class.
:field serial: The serial number in the database.
:field year: The year of the test.
:field semester: The semester the test was taken.
:field specific_date: First, second or the special date.
:field course: The serial number of the course the test is for.
:field questions: A list of the questions in the
:field maker: The lecturer who wrote the test.
"""
    def __init__(self, serial, year, semester, specific_date, course, questions, maker):
        self.serial = serial
        self.year = year
        self.semester = semester
        self.specific_date = specific_date
        self.course = course
        self.questions = list.copy(questions)
        self.maker = maker

    def add_question(self, question):
        self.questions.append(question)

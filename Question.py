class Question:
    """
:field serial: The serial number of the question in the database.
:field test_serial: The serial number of the test the question first appeared in.
:field question_subject: the main subject for this question.
:field question_Sub_subject: the sub subject from the main subject for the question.
:field difficulty: the difficulty of the question.
:field has_answer: does the question have an answer.
:field answer_type: the type of answer (full answer/final answer).
"""
    def __init__(self, serial, file_name, test, question_subject, question_sub_subject, difficulty, has_answer, answer_type):
        self.serial = serial
        self.file_name = file_name
        self.test = test
        self.subject = question_subject
        self.sub_subject = question_Sub_subject
        self.difficulty = difficulty
        self.has_answer = has_answer
        self.answer_type = answer_type

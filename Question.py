from SuperData import SuperData


class Question(SuperData):
    """
:field serial: The serial number of the question in the database.
:field file_name: The name of the file containing the question.
:field test: The serial number of the test the question first appeared in.
:field subject: the main subject for this question.
:field difficulty: the difficulty of the question.
:field has_answer: does the question have an answer.
:field answer_type: the type of answer (full answer/final answer).
:field sub_questions: A list of the sub-questions in the question.
"""
    def __init__(self, serial, file_name, test, subject, difficulty, has_answer, answer_type, sub_questions=[]):
        SuperData.__init__(self, serial)
        self.file_name = file_name
        self.test = test
        self.subject = subject
        self.difficulty = difficulty
        self.has_answer = has_answer
        self.answer_type = answer_type
        self.sub_questions = sub_questions

    def __str__(self):
        return("serial number: " + self.serial)

    def add_sub_question(self, sub):
        for q in self.sub_questions:
            if sub.serial == q.serial:
                return
        self.sub_questions.append(sub)

    def __dict__(self):
        lis = []
        for q in self.sub_questions:
            lis.append(q.serial)
        return {'serial': self.serial,
                'file_name': self.file_name,
                'test': self.test,
                'subject': self.subject,
                'difficulty': self.difficulty,
                'has_answer': self.has_answer,
                'answer_type': self.answer_type,
                'sub_questions': lis}


class SubQuestion(Question):
    def __init__(self, serial, file_name, test, question_subject, question_Sub_subject, difficulty, has_answer, answer_type, relation=True):
        Question.__init__(self, serial, file_name, test, question_subject, question_Sub_subject, difficulty, has_answer, answer_type)
        self.relation = relation

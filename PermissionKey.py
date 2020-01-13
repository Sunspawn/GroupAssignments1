from log import log

class PermissionKey:
    """Permission keys used by staff and students to access the database.
:field access_data: permission to query the database for data.
:field access_questions: permission to change the questions, tests and courses.
:field access_answers: permission to add answers to questions.
:field access_staff: permission to modify staff members.
"""
    def __init__(self, access_data=True, access_questions=True,
                 access_answers=True, access_staff=False):
        self.access_data = access_data
        self.access_questions = access_questions
        self.access_answers = access_answers
        self.access_staff = access_staff
        log("build new permissions key", True)


    def __dict__(self):
        d = dict()
        d["access_data"] = self.access_data
        d["access_questions"] = self.access_questions
        d["access_answers"] = self.access_answers
        d["access_staff"] = self.access_staff
        return d

    def __str__(self):
        return repr(self.__dict__())


def student_key():
    return PermissionKey(access_questions=False, access_answers=False)


def lecturer_key():
    return PermissionKey()


def coordinator_key():
    return PermissionKey(access_staff=True)

class PermissionKey:
    def __init__(self, access_data=True, access_questions=True,
                 access_answers=True, access_staff=False):
        self.access_data = access_data
        self.access_questions = access_questions
        self.access_answers = access_answers
        self.access_staff = access_staff


def student_key():
    return PermissionKey(access_questions=False, access_answers=False)


def lecturer_key():
    return PermissionKey()


def coordinator_key():
    return PermissionKey(access_staff=True)

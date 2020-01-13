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

    def student_key(self):
        return PermissionKey(access_questions=False, access_answers=False)

    def lecturer_key(self):
        return PermissionKey()

    def coordinator_key(self):
        return PermissionKey(access_staff=True)

"""Main menu of the project.
"""

from Database import Database
from Question import Question
from Question import SubQuestion
from PermissionKey import PermissionKey

"""login_keys = {'1': PermissionKey.coordinator_key(),
              '2': PermissionKey.lecturer_key(),
              '3': PermissionKey.student_key()}

login = input("Enter account type:\nCoordinator - 1\n" +
              "Lecturer - 2\nStudent - 3\n")
your_key = login_keys[login]
option = input("Enter what you want to do:\nFind question - 1\nExtract PDF to image - 2\nAdd to image to word file - 3\nAdd a question - 4\n")

if option == '2':
    PDFconvert.convertPDFtoImage()
elif option == '3':
    addImgToDocx.addImgToDocx()
elif option == '4':
    question = Question(12314,"asd","aaa","topic","subject","A",True,"Full")
    manageData.writeData(question)"""

key = PermissionKey.coordinator_key()

q = Question(1, "file", 1, 'sub', 4, True, 'Video')

qq = SubQuestion(2, 'file', 1, 'sub', 5, True, 'Video')

q.add_sub_question(qq)

d = Database()

d.add_question(q, key)

d.writeData(d.questions[0])

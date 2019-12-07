"""Main menu of the project.
"""

import PermissionKey

login_keys = {'1': PermissionKey.coordinator_key(),
              '2': PermissionKey.lecturer_key(),
              '3': PermissionKey.student_key()}

login = input("Enter account type:\nCoordinator - 1\n" +
              "Lecturer - 2\nStudent - 3\n")
your_key = login_keys[login]
option = input("Enter what you want to do:\nFind question - 1\n")

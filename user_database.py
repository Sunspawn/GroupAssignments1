"""
File containing all functions and constants relating to users accessing the system.
"""


def check_login_data(uname, upass):
    """
    Checks the login data according to the user database.
Throws an exception if can't find database file.
:param uname: Username
:param upass: Password
:return: Type of user if available or None if n ot a user.
"""
    result = None
    login_file = open("data/login_data.txt", 'r')
    if login_file.mode == 'r':
        database = login_file.read()
        login_data = database.split(';')
        for line in login_data:
            split_line = line.split(':')
            if (split_line[0] == uname) and (split_line[1] == upass):
                login_file.close()
                result = split_line[2]
                break
    return result
    raise FileNotFoundError

class Question:
    """
:field serial: The serial number of the question in the database.
:field file_name: The name of the image/pdf file in the file directory.
:field test: The serial number of the test the question first appeared.
in.
"""
    def __init__(self, serial, file_name, test):
        if type(file_name) is not str:
            raise TypeError('File name is not a string.')
        self.serial = serial
        self.file_name = file_name
        self.test = test

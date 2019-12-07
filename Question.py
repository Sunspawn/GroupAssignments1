class Question:
    """
:field serial: The serial number of the question in the database.
:field file_name: The name of the image/pdf file in the file directory.
:field test_serial: The serial number of the test the question first appeared
in.
"""
    def __init__(self, serial, file_name, test_serial):
        self.serial = serial
        self.file_name = file_name
        self.test_serial = test_serial

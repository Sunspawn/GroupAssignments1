""" pdf2image uses poppler, you have to download poppler for your OS, and add it's path to the system PATH. """
from pdf2image import convert_from_path

def convertPDFtoImage():
    fileName = input("Enter the name of the pdf file: ")
    pages = convert_from_path(fileName + ".pdf", 500)
    for page in pages:
        page.save(fileName + ".jpg", 'JPEG')
    print("Image saved")
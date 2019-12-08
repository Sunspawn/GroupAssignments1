""" pip install python-docx if missing """

from docx import Document
from docx.shared import Inches

def addImgToDocx():
	fileName = input("Enter the name of the image file: ")
	document = Document() 
	document.add_picture(fileName + ".jpg",width=Inches(15))
	document.save('docTest.docx')
	print("img added to docTest.docx")
	
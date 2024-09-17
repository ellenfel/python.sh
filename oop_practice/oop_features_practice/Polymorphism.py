# Classes
     
class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
     
    def open():
        print("Opening a generic file...")
     
class PDFFile(File):
     
    def __init__(self, name):
        File.__init__(self, name, ".pdf")
     
    def open(self):
        print("Opening a PDF File...")
     
class TextFile(File):
     
    def __init__(self, name):
        File.__init__(self, name, ".txt")
     
    def open(self):
        print("Opening a Text File...")

def open_files(files):
    for file in files:
        file.open()

pdf1 = PDFFile("Brochure")
pdf2 = PDFFile("Course Advertising")
text1 = TextFile("List of Students")

files = [pdf1, text1, pdf2]

open_files(files)

#  This is an example of polymorphism. Calling the same
#  method on instances of different data types that have
#  a method with the same name causes a different effect
#  because the method is implemented differently.
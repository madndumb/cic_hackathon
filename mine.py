from PyPDF2 import PdfFileReader
import docxpy

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        text = ""
        for page in range(pdf.getNumPages()):
            page = pdf.getPage(page)
            text += page.extractText()

        return text

input = 1
text = ""
if(input == 1):
    path = 'sample.pdf'
    text=text_extractor(path)

if(input == 2):
    file = 'sample.docx'
    text = docxpy.process(file)

if(input == 3):
    file = open('sample.txt','r')
    lines = file.readlines()
    file.close()

    for line in lines:
        text += line

print(text)

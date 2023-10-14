from PyPDF2 import PdfReader
from docx import Document

reader = PdfReader("will.pdf")
page = reader.pages[1]
print(page.extract_text())


# # opening pdf file in read binary mode
# with open('Thesis_Guy_zaidner.pdf','rb') as f:
#     # create pdf object
#     pdf = PyPDF2.PdfReader(f)

#     document = Document()

#     for page in range(len(pdf.pages)):
#         print(page)
#         text = pdf.pages[page].extract_text()
#         print(text)
#         document.add_paragraph(text)
# document.save('will.docx')
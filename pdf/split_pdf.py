"""
Writes out two-page documents from one big pdf file
"""
from PyPDF2 import PdfFileWriter, PdfFileReader

with open("CLEAR_Stakeholder_Letter.pdf", "rb") as pdf_file:

    input_pdf = PdfFileReader(pdf_file)

    for page in range(input_pdf.numpages / 2):

        pages = (2 * page, (2 * page) + 1)

        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(pages[0]))
        output.addPage(input_pdf.getPage(pages[1]))

        with open("./split/CLEAR_Stakeholder_Letter_%s.pdf" % page, "wb") as outputStream:
            output.write(outputStream)
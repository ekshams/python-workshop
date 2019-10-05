import PyPDF4
reader = PyPDF4.PdfFileReader('sample10.pdf')
for pagenum in range(reader.numPages):
    page = reader.getPage(pagenum)
    text = page.extractText()
    print(text)
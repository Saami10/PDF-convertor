import PyPDF2
#import collections  
pdf_file=open('ch.pdf','rb')
read_file=PyPDF2.PdfFileReader(pdf_file)
numpage=read_file.getNumPages()
#c=collections.Counter(range(numpage))
for i in range(numpage):
    page=read_file.getPage(i)
    page_content=page.extractText()
    page_content=page_content.replace("\n","")
    print(page_content.encode('utf-8'))

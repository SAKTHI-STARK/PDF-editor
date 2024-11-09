import PyPDF2
import select_directory as sd
import split_pdf as sp
import merge_pdf as mp
#funtion for split the pdf from certain renge to range
def add_pdf(input_pdf_1,iput_pdf_2,page):
    pdf_writer = PyPDF2.PdfWriter()
    sp.split_pdf(input_pdf_1,1,page)
    #saving the newly created pdf file
    with open(sd.save_file(), 'wb') as output_file:
        pdf_writer.write(output_file)
page=int(input("enter page no to add:"))
add_pdf(sd.select_file(),sd.select_file(),page)  

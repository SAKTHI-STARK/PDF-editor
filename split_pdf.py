import PyPDF2
import select_directory as sd
#funtion for split the pdf from certain renge to range
def split_pdf(input_pdf, start_page, end_page):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()
    #for loop for adding the certain range pages from the pdf
    for page_num in range(start_page - 1, end_page):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)
    #saving the newly created pdf file
    with open(sd.save_file(), 'wb') as output_file:
        pdf_writer.write(output_file)

split_pdf(sd.select_file(), 1, 6)  

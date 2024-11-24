import PyPDF2
import select_directory as sd
# Function to save the newly created PDF file
pdf_writer = PyPDF2.PdfWriter()
def savefile():
    with open(sd.save_file(), 'wb') as output_file:
        pdf_writer.write(output_file)
        output_file.close()
# Function to split the PDF from a certain range to range
def split_pdf(input_pdf, start_page, end_page):
    # Ensure input_pdf is a file path or file-like object
    if isinstance(input_pdf, str):
        pdf_reader = PyPDF2.PdfReader(input_pdf)
    elif hasattr(input_pdf, 'read'):
        pdf_reader = PyPDF2.PdfReader(input_pdf)
    else:
        raise ValueError("input_pdf should be a file path or file-like object")
    # For loop for adding the certain range pages from the PDF
    for page_num in range(start_page - 1, end_page):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)
    # Save the newly created PDF file
    savefile()
    


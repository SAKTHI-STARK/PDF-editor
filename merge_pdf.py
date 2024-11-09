import PyPDF2
import select_directory as sd
#declaring global variables
global pdf_files
#function for initial selecing files
def select_pdf():
    global pdf_files
    pdf_files = sd.select_file()
    print(pdf_files)
def add_pages():
    global pdf_files
    new_file=sd.select_file()
    pdf_files.extend(new_file)
    print(pdf_files)
    merge_pdfs(pdf_files)
#function to merge the multiple pdf into one
def merge_pdfs(pdf_list):
    print(pdf_list)
    pdf_merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        pdf_merger.append(pdf)
    with open(sd.save_file(), 'wb') as output_file:
        pdf_merger.write(output_file)


select_pdf()
add_pages()
import PyPDF2
import select_directory as sd
 
def add_pdf_in_middle(main_pdf_path, insert_pdf_path, page):
    # Open the main PDF and the PDF to be inserted
    main_pdf = PyPDF2.PdfReader(main_pdf_path)
    insert_pdf = PyPDF2.PdfReader(insert_pdf_path)
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add pages from the main PDF up to the middle index
    for page_num in range(page):
        page = main_pdf.pages(page_num)
        pdf_writer.addPage(page)
    
    # Add all pages from the insert PDF
    for page_num in range(insert_pdf.getNumPages()):
        page = insert_pdf.pages(page_num)
        pdf_writer.addPage(page)
    
    # Add the remaining pages from the main PDF
    for page_num in range(page, main_pdf.getNumPages()):
        page = main_pdf.pages(page_num)
        pdf_writer.addPage(page)
    
    # Write the output PDF to a file
    with open(sd.save_file(), 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)

# Example usage
page=int(input("enter page no u want to add:"))
main_pdf=sd.select_file()
insert_pdf=sd.select_file()
add_pdf_in_middle(main_pdf,insert_pdf , page)

import tkinter as tk
from tkinter import *
from tkinter.font import Font
import select_directory as sd
import split_pdf as sp
window = tk.Tk()

# Function to create a new window for each functionality
def create_new_window(title):
    new_window = Toplevel(window)
    window_title = title
    new_window.title(window_title)
    new_window.geometry("300x200")
#condition to check which button is clicked
    if title == "split Pdf":
        #function for the new window after clicked the select file button
        def get_page_vals(input_pdf):
            Button_select.pack_forget()
            Start_page = tk.Label(new_window, text="Start Pg No:")
            Start_page.pack()
            start_page_val = tk.Entry(new_window)
            start_page_val.pack()
            End_page = tk.Label(new_window, text="End Page No:")
            End_page.pack()
            End_page_val = tk.Entry(new_window)
            End_page_val.pack()
            #separately write function to get the page number entries
            def split_pdf_command():
                st_pg_val = int(start_page_val.get())
                End_pg_val = int(End_page_val.get())
                sp.split_pdf(input_pdf, st_pg_val, End_pg_val)
                new_window.quit()
            
            Button_convert = Button(new_window, text="Split PDF", fg="RED", width=20, height=2, command=split_pdf_command)
            Button_convert.pack(pady=20)
        #function for select the source pdf file
        def select_file():
            try:
                input_pdf = sd.select_file()
                get_page_vals(input_pdf)
            except Exception as e:
                print(f"An error occurred: {e}")
        Button_select = Button(new_window, text="Select PDF", fg="RED", width=20, height=2, command=select_file)
        Button_select.pack(pady=20)
    elif title == "Image to PDF":
        pass
    elif title == "Merge PDF":
        pass
    elif title == "ADD PDF Pages":
        pass
# Function to create the main window to display all functionalities
def main_window(Name_app, author_name):
    # to disappear existing text in the window
    Name_app.place_forget()
    author_name.place_forget()
    # to resize the loading window to main window
    window.geometry("600x400")
    window.configure(bg="blanchedalmond")
    # tkinter window customization
    def main_window_elements():
        # display PDF EDITOR in the main window
        Header_font = Font(size=22, weight='bold')
        Header = tk.Label(window, text="PDF EDITOR", bg="blanchedalmond", fg="deeppink4", font=Header_font)
        Header.pack()
        # creating buttons to call functions
        Button_split = Button(window, text="Split PDF", fg="RED", width=20, height=2, command=lambda: create_new_window("split Pdf"))
        Button_split.pack(pady=20)
        Button_i2p = Button(window, text="Image to PDF", fg="RED", width=20, height=2, command=lambda: create_new_window("Image to PDF Converter"))
        Button_i2p.pack(pady=20)
        Button_merge = Button(window, text="Merge PDF", fg="RED", width=20, height=2, command=lambda: create_new_window("Merge PDF"))
        Button_merge.pack(pady=20)
        Button_add_pages = Button(window, text="Add PDF", fg="RED", width=20, height=2, command=lambda: create_new_window("ADD PDF Pages"))
        Button_add_pages.pack(pady=20)
    main_window_elements()
# Function for loading window
def loading_window():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    window.title("PDF-EDITOR")
    # creating name for our app name
    App_name_font = Font(size=30, weight='bold')
    App_name = tk.Label(window, text="PDF-EDITOR", bg="blanchedalmond", fg="deeppink4", font=App_name_font)
    App_name.place(x=110, y=65)
    # creating author name for our app
    Author_name_font = Font(size=10, weight='bold')
    author_name = tk.Label(window, text="by SAKTHI-STARK", bg="blanchedalmond", fg="deeppink4", font=Author_name_font)
    author_name.place(x=230, y=110)
    # transforming window to new size
    window.after(700, lambda: main_window(App_name, author_name))
    window.mainloop()
loading_window()

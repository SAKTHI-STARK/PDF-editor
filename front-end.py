import tkinter as tk
from tkinter import *
from tkinter.font import Font
import select_directory as sd
import split_pdf as sp
window = tk.Tk()

# Function to create a new window for each functionality
def create_new_window(title):
    new_window = Toplevel(window)
    window_title=title
    new_window.title(window_title)
    new_window.geometry("300x200")
    if title=="split Pdf":
        def select_file():
            file_path=sd.select_file()
            print(file_path)
           
            def split_file(file_path):
                sp.split_pdf(file_path,1,4)
            split_file(file_path) 
        Button_merge = Button(new_window, text="Select PDF", fg="RED", width=20, height=2,command=select_file)
        Button_merge.pack(pady=20)
        # start_page=tk.Label(new_window,text="start page no:")
        # start_page.pack()
        # start_pg_val=tk.Entry(new_window)
        # start_pg_val.place(x=120,y=25)
        # Button_merge = Button(new_window, text="Split PDF", fg="RED", width=20, height=2)
        # Button_merge.pack(pady=20)
        # Button_merge = Button(new_window, text="Save PDF", fg="RED", width=20, height=2)
        # Button_merge.pack(pady=20)
        pass
    elif title=="Image to PDF":
        
        pass
    elif title=="Merge PDF":
       
        pass
    elif title=="ADD PDF Pages":
       
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
        Button_split = Button(window, text="Split PDF", fg="RED", width=20, height=2, command=lambda:create_new_window("split Pdf"))
        Button_split.pack(pady=20)
        Button_i2p = Button(window, text="Image to PDF", fg="RED", width=20, height=2, command=lambda:create_new_window("Image to PDF Converter"))
        Button_i2p.pack(pady=20)
        Button_merge = Button(window, text="Merge PDF", fg="RED", width=20, height=2, command=lambda:create_new_window("Merge PDF"))
        Button_merge.pack(pady=20)
        Button_add_pages = Button(window, text="Add PDF", fg="RED", width=20, height=2, command=lambda:create_new_window("ADD PDF Pages"))
        Button_add_pages.pack(pady=20)
    main_window_elements()

# Function for loading window
def loading_window():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    # icon for our app title
    icon = PhotoImage(file="SV.png")
    window.iconphoto(True, icon)
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

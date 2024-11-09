import tkinter as tk
from tkinter import *
from tkinter.font import Font
window = tk.Tk()
#creating main window to display all functionalities
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
        Button_split = Button(window, text="Split PDF", fg="RED", width=20, height=2)
        Button_split.pack(pady=20)
        Button_i2p = Button(window, text="Image to PDF", fg="RED", width=20, height=2)
        Button_i2p.pack(pady=20)
        Button_merge = Button(window, text="Merge PDF", fg="RED", width=20, height=2)
        Button_merge.pack(pady=20)
        Button_add_pages = Button(window, text="Add PDF", fg="RED", width=20, height=2)
        Button_add_pages.pack(pady=20)
    main_window_elements()
#function for loading window
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
#creating window for split pdf function
def clear_button(Button_add_pages,Button_merge,Button_i2p,Button_split):
    Button_add_pages.pack_forget()
    Button_merge.pack.forget()
    Button_i2p.pack.forget()
    Button_split.pack.forget()
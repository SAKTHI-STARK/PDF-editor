import tkinter as tk
from tkinter import *
from tkinter.font import Font
window=tk.Tk()

def main_window(Name_app,author_name):
    #to dissapear existing text in the window
    Name_app.place_forget()
    author_name.place_forget()
    #to resize the loading window to main window
    window.geometry("600x400")
    #tkinter window customization
    def main_window_elements():
        #display flames calculator in the main window
        Header_font=Font(size=22,weight='bold')
        Header=tk.Label(window,text="PDF EDITOR",bg="blanchedalmond",fg="deeppink4",font=Header_font)
        Header.place(x=150,y=20)
        #creating button to call function
        Button_calculate=Button(window,text="Find",fg="RED")
        Button_calculate.place(x=300,y=160)
        Button_clear=Button(window,text="Clear",fg="RED")
        Button_clear.place(x=340,y=160)
    main_window_elements()
def loading_window():
    window.geometry("400x200")
    window.configure(bg="blanchedalmond")
    #icon for our app title
    icon=PhotoImage(file="SV.png")
    window.iconphoto(True,icon)
    window.title("PDF-EDITOR")
    #creating name for our app name
    App_name_font=Font(size=30,weight='bold')
    App_name=tk.Label(window,text="PDF-EDITOR",bg="blanchedalmond",fg="deeppink4",font=App_name_font)
    App_name.place(x=110,y=65)
    #creating author name for our app
    Author_name_font=Font(size=10,weight='bold')
    author_name=tk.Label(window,text="by SAKTHI-STARK",bg="blanchedalmond",fg="deeppink4",font=Author_name_font)
    author_name.place(x=153,y=110)
    #transforming window to new size 
    window.after(700,lambda:main_window(App_name,author_name))
    window.mainloop()
loading_window()


import tkinter as tk
from tkinter import filedialog
#function for selecting the file source directory
def select_file():
    select_window = tk.Tk()
    select_window.withdraw()  # Hide the root window
    file_path = list(filedialog.askopenfilenames())
    return file_path
#function to select the file saving directory
def save_file():
    save_window = tk.Tk()
    save_window.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".pdf",  # Default extension for the saved file
        filetypes=[("Text Files", ".pdf"), ("All Files", ".*")]
    )
    return file_path


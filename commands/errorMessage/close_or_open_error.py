import tkinter
from tkinter import messagebox

tk = tkinter.Tk()

def show_error():
    messagebox.showerror('Error', 'Digite "close" ou "open"')

tk.title("Error Message")
show_error()


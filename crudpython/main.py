# main.py

from tkinter import *
from view import App
from styles import App
import banco

if __name__ == "__main__":
    banco.create_table()  # This ensures the table is created (if it doesn't already exist) before the app starts
    style_buttons()
    root = Tk()
    app = App(root)
    root.mainloop()


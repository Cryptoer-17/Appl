import tkinter as tk
from tkinter import *
import requests
from object_class_gui import Application
#from window import class_method
#creazione dell'oggetto TK()
#win = tk.Tk()
#window = class_method(win,"ASCII ART DOWNLOADER","1030x570")


root = Tk()
root.overrideredirect(1)
"""root.title("Lazy button")"""
root.geometry("1200x730")
root.geometry("+250+130")
root.grid_columnconfigure(0,weight=3)


app = Application(root)

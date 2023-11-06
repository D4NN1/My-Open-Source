import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


window = tk.Tk()
window.geometry("500x500")
window.title("ToDoList")

rows = 1
srow = rows 

def addEntry():
    global rows
    global srow
    ToDoListEntry = ListEntry.get()
    if ToDoListEntry:
        Entries = tk.Label(text=ToDoListEntry)
        Entries.grid(column=1, row=rows)
        entries_list.append(ToDoListEntry)
        ListEntry.delete(0, 'end')  
        removeButton = tk.Button(window, text="Remove", command=removeEntry)
        removeButton.grid(column=2, row=rows)
        rows += 1
        srow = rows 

def removeEntry():
     global rows
     global srow
     srow-=1
     widget = window.grid_slaves(row=srow, column=1)[0]
     widget.destroy()
     widget2 = window.grid_slaves(row=srow, column=2)[0]
     widget2.destroy()
     
ListEntry = tk.Entry(window)
ListEntry.grid(column=0, row=0)
addButton = tk.Button(window, text="Add", command=addEntry)
addButton.grid(column=1, row=0)

entries_list = []

window.mainloop()

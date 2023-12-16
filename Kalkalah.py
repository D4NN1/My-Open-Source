import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
window = tk.Tk()
window.geometry("500x500")
window.title("Age Calculator")
Name = tk.Label(text="Name")
Name.grid(column=0,row=1)
Year = tk.Label(text="Year")
Year.grid(column=0,row=2)
Month = tk.Label(text="Month")
Month.grid(column=0,row=3)
Day = tk.Label(text="Day")
Day.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
def getInput():
    name=nameEntry.get()
    monkey = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Pissing our pants yet {persons}!!!. You are {age} years old!!!  I dont kill kids so that something to consider".format(persons=name, age=monkey.age())
    textArea.insert(tk.END,answer)
button=tk.Button(window,text="Kalpulate ur Age",command=getInput,bg="darkblue")
button.grid(column=1,row=5)
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
image=Image.open('Negan.png')
image.thumbnail((300,300),Image.BILINEAR)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)
window.mainloop()

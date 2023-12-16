import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
class Operators:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.result = 0
    def add(self):
        self.result = self.x + self.y
        return self.result
    def multiply(self):
        self.result = self.x * self.y
        return self.result
    def divide(self):
        self.result = self.x / self.y
        return self.result
    def subtract(self):
        self.result = self.x - self.y
        return self.result



def getInput():
    augend = float(augendEntry.get())
    addend = float(addendEntry.get())
    Sum = Operators(augend,addend)
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer =   " The sum is  {result}!!!.".format(result=str(Sum.add()))
    textArea.insert(tk.END, answer)
def getInput1():
    multiplicand = float(multiplicandEntry.get())
    multiplier = float(multiplierEntry.get())
    Product = Operators(multiplicand,multiplier)
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer =   " The product is  {result}!!!.".format(result=str(Product.multiply()))
    textArea.insert(tk.END, answer)
def getInput2():
    minuend = float(minuendEntry.get())
    subtrahend = float(subtrahendEntry.get())
    Difference = Operators(minuend,subtrahend)
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer =   " The difference is  {result}!!!.".format(result=str(Difference.subtract()))
    textArea.insert(tk.END, answer)
def getInput3():
    dividend = float(dividendEntry.get())
    divisor = float(divisorEntry.get())
    Quotient = Operators(divisor,dividend)
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer =   " The quotient is  {result}!!!.".format(result=str(Quotient.divide()))
    textArea.insert(tk.END, answer)
augendEntry = tk.Entry()
augendEntry.grid(column=1,row=1)
addendEntry = tk.Entry()
addendEntry.grid(column=1,row=2)
minuendEntry = tk.Entry()
minuendEntry.grid(column=1,row=3)
subtrahendEntry = tk.Entry()
subtrahendEntry.grid(column=1,row=4)
multiplicandEntry = tk.Entry()
multiplicandEntry.grid(column=1,row=5)
multiplierEntry = tk.Entry()
multiplierEntry.grid(column=1,row=6)
dividendEntry = tk.Entry()
dividendEntry.grid(column=1,row=8)
divisorEntry = tk.Entry()
divisorEntry.grid(column=1,row=7)
print ("First and second lines for addition, third and fourth for subtraction, 5th and 6th for multiplication, anyway ever watch the walking dead")


Entry = tk.Entry()
addendEntry.grid(column=1,row=2)
    
window = tk.Tk()
window.geometry("500x500")
window.title(" Simple Calculator")
Multiply = tk.Button(window, text = "*", command=getInput1,bg = "limegreen")
Add =  tk.Button(window, text = "+", command=getInput,bg = "darkblue")
Subtract  = tk.Button(window, text = "-", command=getInput2,bg = "pink")
Divide = tk.Button(window, text = "/", command=getInput3,bg = "yellow")
Add.grid(column=3,row=5)
Multiply.grid(column=3,row=7)
Divide.grid(column=3,row=8)
Subtract.grid(column=3,row=6)
window.mainloop()

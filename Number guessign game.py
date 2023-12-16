import tkinter as tk
import random 
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.geometry("500x500")
window.title("Number Guessing game")
answer = ("Guess a number between 0 and 100")
text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
text_area.grid(column=0,row=4)
text_area.insert(tk.END,answer)
guess = tk.Entry()
guess.grid(column=0,row=17)
mguess = random.randint(0,100)
def to_guess(tguess):
    tguess = int(guess.get())
    if mguess>tguess:
        hint = "Too Low"
    elif tguess>mguess:
        hint = "Too High"
    elif tguess == mguess:
        hint = "Correct"
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=20)
    text_area.insert(tk.END,hint)
button=tk.Button(window,text="Guess the Number",bg="darkblue")
button.bind("<Button-1>",to_guess)
button.grid(column=0,row=9)
window.mainloop()

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
window.geometry("500x500")
window.title("rock paper scissors")
USER_SCORE = 0
COMP_SCORE = 0
Options = {1: 'rock',
           2: 'paper',
           3: 'scissors',}
def Rock(event):
        USER_SCORE = 0
        COMP_SCORE = 0
        UserPlay = input('rock paper or scissors all in lwrcse')
        ran =  random.randint(1,3)
        if UserPlay == Options[ran]:
            print("we've drawn")
        elif UserPlay == 'rock' and Options[ran] == 'scissors':
            print("you have won")
            USER_SCORE+=1
        elif UserPlay == 'scissors' and Options[ran] == 'paper':
            print("you have won")
            USER_SCORE+=1
        elif UserPlay == 'scissors' and Options[ran] == 'rock':
            print("you have lost")
            COMP_SCORE+=1
        elif UserPlay == 'paper' and Options[ran] == 'scissors':
            print("you have lost")
            COMP_SCORE+=1
        elif UserPlay == 'paper' and Options[ran] == 'rock':
            print("you have won")
            USER_SCORE+=1
        elif UserPlay == 'rock' and Options[ran] == 'paper':
            print("you have lost")
            COMP_SCORE+=1
        elif UserPlay not in Options:
            print('error')
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=UserPlay,cc=Options[ran],u=USER_SCORE,c=COMP_SCORE)    
        text_area.insert(tk.END,answer)
text_area = tk.Text(master=window,height=30,width=30,bg="#FFFF99")
text_area.grid(column=0,row=4)
text = tk.Button(window,text='Rock Paper Scissors',bg = 'blue')
text.grid(column=1,row=1)
text.bind("<Button-1>",Rock)

window.mainloop()






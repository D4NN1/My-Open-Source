import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser
window = tk.Tk()
window.geometry("500x500")
window.title("Bookmark app")
def spotify(event):
    webbrowser.open_new_tab('https://open.spotify.com/playlist/76Uy37A9wEIhW7S6oaYPUg?si=a1d3b52468334898')
AllMyLinks = tk.Label(text="All My Links.")
AllMyLinks.grid(column=0,row=0)
Spotify = tk.Button(window,text='Spotify',bg='darkgreen')
Spotify.grid(column=1,row=1)
Spotify.bind("<Button-1>",spotify)
window.mainloop()

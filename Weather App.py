import tkinter as tk
import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

API_KEY = "aSAwetXZcLC1nI7PxGu5gCKtYEyqgex0"

window = tk.Tk()
window.geometry("500x500")
window.title("Weather App")


CityEntry = tk.Entry()
CityEntry.grid(column=1,row=1)


def Search():
    City = CityEntry.get()
    CitiesList = {"London":328328, "Berlin":178087, "New York":349727}
    url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{CitiesList[City]}?apikey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    day_info = data["DailyForecasts"][0]["Day"]["IconPhrase"]
    night_info = data["DailyForecasts"][0]["Night"]["IconPhrase"]
    Weather = tk.Text(master=window, height=10,width=25)
    Weather.grid(column=1,row=8)
    Report = " Weather(Day): {persons} in {city} Weather(Night):{night} in {city}.".format(persons=day_info,city=City, night = night_info)
    Weather.insert(tk.END,Report)
    if "cloud" in Report or "Cloud" in Report:
        image=Image.open('CloudyDay.jpg')
        image.thumbnail((100,100),Image.BILINEAR)
        photo=ImageTk.PhotoImage(image)
        label_image=tk.Label(image=photo)
        label_image.grid(column=1,row=4)
    elif "Shower" in Report:
        image=Image.open('RainyNight.jpg')
        image.thumbnail((100,100), Image.BILINEAR)
        photo=ImageTk.PhotoImage(image)
        label_image = tk.Label(image=photo)
        label_image.grid(column=3, row=4)

   
Find = tk.Button(window, text="Find", command=Search)
Find.grid(column=1, row=0)

window.mainloop()



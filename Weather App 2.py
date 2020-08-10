import tkinter as tk
from tkinter import font
import requests

HEIGHT=500
WIDTH= 600

def format_reponse(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = "City: %s \nConditions: %s \nTemperature (F): %s" % (name, description, temp)
    except:
        final_str = "There was a problem retrieving the information"

    return final_str


def get_weather(city):
    weather_key = "7605e78761077a6b70267e3e7e86e914"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    reponse = requests.get(url, params)
    weather= reponse.json()

    label['text'] = format_reponse(weather)

root = tk.Tk()

#7605e78761077a6b70267e3e7e86e914
#pro.openweathermap.org/data/2.5/forecast/hourly?id={city ID}&appid={your api key}
#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={your api key}
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="C:/Users/Vishal/Downloads/icon-weather-png-2.png")
backgroung_label= tk.Label(root, image=background_image)
backgroung_label.place(x=0,y=0, relwidth=1, relheight=1)

frame= tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5,rely=0.1, relwidth = 0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Calibri', 15))
entry.place(relwidth=0.65, relheight=1, )

button = tk.Button(frame, text = "Get Weather", font=('Calibri', 15), command=lambda : get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_Frame= tk.Frame(root, bg="#80c1ff", bd=10)
lower_Frame.place(relx=0.5,rely=0.25, relwidth = 0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_Frame, font=('Calibri', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()

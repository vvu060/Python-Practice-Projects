from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.iconbitmap("F:/Python Codes/TKINTER/weather.ico")
root.geometry("600*100")
root.configure(background=weather_color)

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=10&API_KEY=41799037-BC4F-4865-B2F1-B8E3EEDA036D

# Create Ziplookup Fun
def ziplookup():
    #zip.get()
    #zipLabel =Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan = 2)

    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=10&API_KEY=41799037-BC4F-4865-B2F1-B8E3EEDA036D")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = '#0C0'
        elif category == "Moderate":
            weather_color = '#FFFF00'
        elif category == "Unheathy for Sernsitive Groups":
            weather_color = '#ff9900'
        elif category == "Unhealthy":
            weather_color = '#FF0000'
        elif category == "Very Unhealthy":
            weather_color = '#990066'
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        my_Lable = Label(root, text=city + "Air Quality" + str(quality) + " " + category, font=("Calibri", 20),background=weather_color)
        my_Lable.grid(row=1, column=0, columnspan = 2)

        zip = Entry(root)
        zip.pack()
        submit_btn = Button(root, text="Submit", command=ziplookup)
        submit_btn.pack()

        except EXCEPTION as e:
        print("Error...")


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)
submit_btn = Button(root, text="Submit", command=ziplookup)
submit_btn.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("900x600+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")
        # print(result)

        # Weather API
        api = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=d58df482a415adfbeaa82380c250ecd6"
        )

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        tempt = int(json_data["main"]["temp"] - 273.15)
        feels_like = int(json_data["main"]["feels_like"] - 273.15)
        press = json_data["main"]["pressure"]
        humid = json_data["main"]["humidity"]
        wind_1 = json_data["wind"]["speed"]

        temp.config(text=(tempt, "°"))
        cond.config(text=(condition, "|", "FEELS", "LIKE", feels_like, "°"))
        wind.config(text=wind_1)
        humidity.config(text=humid)
        pressure.config(text=press)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Input!")


# Search Box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=220, y=20)

textfield = tk.Entry(
    root,
    justify="center",
    width=17,
    font=("Times New Roman", 24, "bold"),
    bg="#404040",
    fg="white",
    border=0,
)
textfield.place(x=240, y=40)
textfield.focus()

# Search Icon
Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(
    image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather
)
myimage_icon.place(x=600, y=32)

# Resizing the image
image = Image.open("logo.png")
# Resize the image using resize() method
resize_image = image.resize((250, 250))

# Logo
Logo_image = ImageTk.PhotoImage(resize_image)
logo = Label(image=Logo_image)
logo.size
logo.place(x=325, y=165)

# Bottom Box
Frame_image = PhotoImage(file="box.png")
frame_myimg = Label(image=Frame_image)
frame_myimg.place(x=10, y=450)
frame_myimg.pack(side=BOTTOM)

# Time
name = Label(root, font=("arial", 16, "bold"))
name.place(x=380, y=100)
clock = Label(root, font=("Georgia", 20, "bold"))
clock.place(x=390, y=130)

# Labels
# Label 1
label1 = Label(
    root, text="WIND", font=("Georgia", 16, "bold"), fg="white", bg="#1ab5ef"
)
label1.place(x=180, y=510)
# Label 2
label1 = Label(
    root, text="HUMIDITY", font=("Georgia", 16, "bold"), fg="white", bg="#1ab5ef"
)
label1.place(x=370, y=510)
# Label 3
label1 = Label(
    root, text="PRESSURE", font=("Georgia", 16, "bold"), fg="white", bg="#1ab5ef"
)
label1.place(x=620, y=510)

# Temp and Condition
temp = Label(font=("Times New Roman", 40, "bold"), fg="#ee666d")
temp.place(x=420, y=410)
cond = Label(font=("Times New Roman", 16, "bold"))
cond.place(x=350, y=470)


# Fetched Values
wind = Label(text="....", font=("Times New Roman", 18, "bold"), bg="#1ab5ef")
wind.place(x=202, y=540)
humidity = Label(text="....", font=("Times New Roman", 18, "bold"), bg="#1ab5ef")
humidity.place(x=420, y=540)
pressure = Label(text="....", font=("Times New Roman", 18, "bold"), bg="#1ab5ef")
pressure.place(x=670, y=540)

root.mainloop()
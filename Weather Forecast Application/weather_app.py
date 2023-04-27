from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


# app window
root = Tk()
root.title("Weather Forecast App")
root.geometry("999x666+300+300")
root.configure(bg="#aee4f2")
root.resizable(False, False)

# getWeather()
def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude) #stores latitide and longitude value

    timezone.config(text=result)
    long_lat.config(
        text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p") #current time at that place
    clock.config(text=current_time)

    # weather
    api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(
        location.longitude)+"&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79" #request data from api 
    json_data = requests.get(api).json() #gets data in json format from api

    # current
    temp = json_data['current']['temp']  
    humidity = json_data['current']['humidity'] 
    pressure = json_data['current']['pressure']  
    wind = json_data['current']['humidity'] 
    description = json_data['current']['weather'][0]['description'] 
    feels_like = json_data['current']['feels_like']  
    visibility = json_data['current']['visibility']
    uvi = json_data['current']['uvi']
    clouds = json_data['current']['clouds']
    dew_point = json_data['current']['dew_point']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=(description))
    f.config(text=(feels_like, "°C"))
    v.config(text=(visibility, "m"))
    u.config(text=(uvi))
    c.config(text=(clouds, "%"))
    d_point.config(text=(dew_point, "°"))

    #################################
    # first day weather
    firstdayimg = json_data['daily'][0]['weather'][0]['icon']
    img = (Image.open(
        f"S:\Weather App Project\live img icon\{firstdayimg}@2x.png"))
    resized_image = img.resize((180, 180))
    photo1 = ImageTk.PhotoImage(resized_image)
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day:{int(tempday1)}°C   Night:{int(tempnight1)}°C")

    # second day
    secondimg = json_data['daily'][1]['weather'][0]['icon']
    photo2 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{secondimg}@2x.png")
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{int(tempday2)}°C  Night:{int(tempnight2)}°C")

    # third day weather
    thirdimg = json_data['daily'][2]['weather'][0]['icon']
    photo3 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{thirdimg}@2x.png")

    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{int(tempday3)}°C  Night:{int(tempnight3)}°C")

    # fourth day weather
    fourthimg = json_data['daily'][3]['weather'][0]['icon']
    photo4 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{fourthimg}@2x.png")
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{int(tempday4)}°C  Night:{int(tempnight4)}°C")

    # fifth day weather
    fifthimg = json_data['daily'][4]['weather'][0]['icon']
    photo5 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{fifthimg}@2x.png")
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{int(tempday5)}°C  Night:{int(tempnight5)}°C")

    # sixth day weather
    sixthimg = json_data['daily'][5]['weather'][0]['icon']
    photo6 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{sixthimg}@2x.png")
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{int(tempday6)}°C  Night:{int(tempnight6)}°C")

    # seventh day weather
    seventhimg = json_data['daily'][6]['weather'][0]['icon']
    photo7 = ImageTk.PhotoImage(
        file=f"S:\Weather App Project\live img icon\{seventhimg}@2x.png")
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{int(tempday7)}°C  Night:{int(tempnight7)}°C")

    # display all days
    first = datetime.now(pytz.timezone(result))
    cell1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    cell2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    cell3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    cell4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    cell5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    cell6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    cell7.config(text=seventh.strftime("%A"))

#Popup function to view developer details
def open_popup():
    top = Toplevel(root)
    top.geometry("600x450")
    top.title("Developer Details")
    top.resizable(False, False)
    
    popup_img = PhotoImage(file="S:\Weather App Project\dev.png")
    popup_image = Label(top, image=popup_img)
    popup_image.place(x=0, y=0)
    top.mainloop()

###########################################################################
# icon
img_icon = PhotoImage(file="S:\Weather App Project\icon.png")
root.iconphoto(False, img_icon)

# rainbow boxes
rainbow_box = PhotoImage(file="S:\Weather App Project\weather details2.png")
Label(root, image=rainbow_box, bg="#aee4f2").place(x=10, y=95)

############################################################################

# label
label1 = Label(root, text="Visibility", font=(
    'Comic Sans MS', 11), fg="black", bg="#8cff8c")
label1.place(x=50, y=281)

label2 = Label(root, text="Humidity", font=(
    'Comic Sans MS', 11), fg="black", bg="#ff925e")
label2.place(x=50, y=165)

label3 = Label(root, text="Pressure", font=(
    'Comic Sans MS', 11), fg="black", bg="#ffff2f")
label3.place(x=50, y=223)

label4 = Label(root, text="Wind Speed", font=(
    'Comic Sans MS', 11), fg="black", bg="#ff7171")
label4.place(x=38, y=109)

label5 = Label(root, text="UV Index", font=(
    'Comic Sans MS', 11), fg="black", bg="#80ffff")
label5.place(x=50, y=339)

label6 = Label(root, text="Clouds", font=(
    'Comic Sans MS', 11), fg="black", bg="#4651ce")
label6.place(x=50, y=397)

label7 = Label(root, text="Dew Point", font=(
    'Comic Sans MS', 11), fg="black", bg="#f900f9")
label7.place(x=50, y=455)

##################################################################
# Weather Forecast text
wf_text = PhotoImage(file="S:\Weather App Project\weatext.png")
weaimage = Label(image=wf_text, bg="#aee4f2")
weaimage.place(x=333, y=10)

# search box
search_box = PhotoImage(file="S:\Weather App Project\search box.png")
myimage = Label(image=search_box, bg="#aee4f2")
myimage.place(x=277, y=120)

# search box cloud image
weat_image = PhotoImage(file="S:\Weather App Project\Layer 7.png")
weatherimg = Label(root, image=weat_image, bg='#203243')
weatherimg.place(x=290, y=128)

# Entry Text Field
textfield = tk.Entry(root, justify='center', width=20, font=(
    'poppins', 20, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=360, y=135)
textfield.focus()

# search icon
search_icon = PhotoImage(file="S:\Weather App Project\Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2",
                      bg="#203243", command=getWeather)
myimage_icon.place(x=655, y=125)
root.bind('<Return>',lambda event:getWeather())  #Enter key to search 

# thinking man
man = PhotoImage(file="S:\Weather App Project\man-t32.png")
Label_man = Label(root, image=man, bg="#aee4f2")
Label_man.place(x=720, y=210)

label_tm = Label(root, text="Feels Like...", font=(
    'Comic Sans MS', 16), fg="black", bg="#ffffff")
label_tm.place(x=825, y=240)

# Bottom Box
firstbox = PhotoImage(file="S:\Weather App Project\dbottom gbox.png")
Label11 = Label(root, image=firstbox, bg="#aee4f2")
Label11.place(x=15, y=500)

Label12 = Label(root, image=firstbox, bg="#aee4f2")
Label12.place(x=179, y=500)

Label13 = Label(root, image=firstbox, bg="#aee4f2")
Label13.place(x=343, y=500)

Label14 = Label(root, image=firstbox, bg="#aee4f2")
Label14.place(x=507, y=500)

Label15 = Label(root, image=firstbox, bg="#aee4f2")
Label15.place(x=671, y=500)

Label16 = Label(root, image=firstbox, bg="#aee4f2")
Label16.place(x=835, y=500)

# clock
clock = Label(root, font=("Comic Sans MS", 25, 'bold'),
              fg="black", bg="#aee4f2")
clock.place(x=20, y=0)

# timezone
timezone = Label(root, font=("Comic Sans MS", 13),
                 fg="black", bg="#aee4f2")
timezone.place(x=815, y=50)

long_lat = Label(root, font=("Comic Sans MS", 12),
                 fg="black", bg="#aee4f2")
long_lat.place(x=810, y=80)


# printing live details
t = Label(root, font=("Comic Sans MS", 40), fg="black",
          bg="#aee4f2")  # prints temperature
t.place(x=400, y=195)

f = Label(root, font=("Comic Sans MS", 15), fg="black", bg="#ffffff")
f.place(x=835, y=270)

h = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#ff925e")
h.place(x=125, y=165)

p = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#ffff2f")
p.place(x=120, y=223)

w = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#ff7171")
w.place(x=127, y=109)

u = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#80ffff")
u.place(x=127, y=339)

d = Label(root, font=("Comic Sans MS", 20), fg="black", bg="#aee4f2")
d.place(x=425, y=275)

v = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#8cff8c")
v.place(x=120, y=280)

c = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#4651ce")
c.place(x=127, y=397)

d_point = Label(root, font=("Comic Sans MS", 11), fg="black", bg="#f900f9")
d_point.place(x=128, y=455)


################################################################################


# first cell
cell1 = Label(root, font=("Comic Sans MS", 25, 'bold'),
              bg="#aee4f2", fg="black")
cell1.place(x=30, y=40)

firstimage = Label(root, bg="#aee4f2")
firstimage.place(x=410, y=315)

day1temp = Label(root, font=("Comic Sans MS", 13),
                 bg="#aee4f2", fg="black")
day1temp.place(x=410, y=465)

# second cell
cell2 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell2.place(x=55, y=505)

secondimage = Label(root, bg="#ded5c1")
secondimage.place(x=40, y=530)

day2temp = Label(root, bg="#ded5c1", fg="black")
day2temp.place(x=28, y=620)

# third cell
cell3 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell3.place(x=219, y=505)

thirdimage = Label(root, bg="#ded5c1")
thirdimage.place(x=204, y=530)

day3temp = Label(root, bg="#ded5c1", fg="black")
day3temp.place(x=192, y=620)

# fourth cell
cell4 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell4.place(x=383, y=505)
fourthimage = Label(root, bg="#ded5c1")
fourthimage.place(x=368, y=530)
day4temp = Label(root, bg="#ded5c1", fg="black")
day4temp.place(x=356, y=620)

# fifth cell
cell5 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell5.place(x=547, y=505)
fifthimage = Label(root, bg="#ded5c1")
fifthimage.place(x=532, y=530)
day5temp = Label(root, bg="#ded5c1", fg="black")
day5temp.place(x=520, y=620)

# sixth cell
cell6 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell6.place(x=711, y=505)
sixthimage = Label(root, bg="#ded5c1")
sixthimage.place(x=696, y=530)
day6temp = Label(root, bg="#ded5c1", fg="black")
day6temp.place(x=684, y=620)

# seventh cell
cell7 = Label(root, font=("Comic Sans MS", 11, 'bold'),
              bg="#ded5c1", fg="black")
cell7.place(x=875, y=505)
seventhimage = Label(root, bg="#ded5c1")
seventhimage.place(x=860, y=530)
day7temp = Label(root, bg="#ded5c1", fg="black")
day7temp.place(x=848, y=620)

##############################
i_button = PhotoImage(file="S:\Weather App Project\info button.png")
ibutton_icon = Button(image=i_button, borderwidth=0, cursor="hand2",
                      bg="#aee4f2", command=open_popup)
ibutton_icon.place(x=950, y=5)

root.mainloop()

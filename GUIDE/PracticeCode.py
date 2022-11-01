from tkinter import *
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

#app window
root = Tk()
root.title("Weather Forecast App")
root.geometry("800x500+300+300")
root.configure(bg="#57adff")
root.resizable(True, True)

#icon
img_icon=PhotoImage(file="S:\Weather App Project\icon.png")
root.iconphoto(False,img_icon)

#round box 
round_box=PhotoImage(file="S:\Weather App Project\Rounded Rectangle.png")
Label(root,image=round_box,bg="#57adff").place(x=30,y=110)

#label
label1=Label(root,text="Temperature",font=('Arial',12),fg="white",bg="#203243")
label1.place(x=75,y=120)

label2=Label(root,text="Humidity",font=('Arial',12),fg="white",bg="#203243")
label2.place(x=75,y=140)

label3=Label(root,text="Pressure",font=('Arial',12),fg="white",bg="#203243")
label3.place(x=75,y=160)

label4=Label(root,text="Wind Speed",font=('Arial',12),fg="white",bg="#203243")
label4.place(x=75,y=180)

label5=Label(root,text="Description",font=('Arial',12),fg="white",bg="#203243")
label5.place(x=75,y=200)

#search box
search_img=PhotoImage(file="S:\Weather App Project\Rounded Rectangle 3.png")
myimage=Label(image=search_img,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="S:\Weather App Project\Layer 7.png")
weatherimg=Label(root,image=weat_image,bg='#203243')
weatherimg.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="S:\Weather App Project\Layer 6.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243")
myimage_icon.place(x=645,y=125)


####Add press enter key to search


root.mainloop()

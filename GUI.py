import tkinter as tk
from tkinter import NW

import cv2

import instructions as instructions
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

from PIL.ImageTk import PhotoImage

root = tk.Tk()

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

def upload():
    browse.set("loading...")
    file = askopenfile(parent=root,mode="rb",title="Choose an image",filetypes =[("JPG file","*.jpg"),("PNG file","*.png"),("JPEG file","*.jpeg"),("All files","*.")])
    if file:

        # photo = PhotoImage(file=file)
        # gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
        # gray = cv2.medianBlur(gray, 5)
        # edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        # color = cv2.bilateralFilter(photo,9,250,250)
        # cartoon = cv2.bitwise_and(color,color,mask=edges)
        photo = Image.open(file)
        gray = photo.convert("L").save("gray.jpg")
        photo = ImageTk.PhotoImage(photo)
        label = tk.Label(image=photo)
        label.image = gray
        label.grid(row=3, column=1, padx=5, pady=5)


intructions = tk.Label(root,text= "Select an image",font = "Raleway")
instructions.grid(columnspan=3,column=0,row=1)


browse = tk.StringVar()
browse_button = tk.Button(root,textvariable = browse,command = lambda:upload(),font = "Raleway",bg="#a022e0",fg ="white",width=15,height =2)

# browse = tk.StringVar()
# browse_button = tk.Button(root,textvariable = browse,command = lambda:upload(),font = "Raleway",bg="#a022e0",fg ="white",width=15,height =2)
browse.set("Browse")
browse_button.grid(column=1,row=2)

canvas = tk.Canvas(root,width = 600,height = 300)
canvas.grid(columnspan = 3)
root.mainloop()







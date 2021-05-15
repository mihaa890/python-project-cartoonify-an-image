import tkinter as tk
from tkinter.ttk import Label

import cv2

from PIL import Image,ImageTk
from tkinter import filedialog


root = tk.Tk()

logo = Image.open('images/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)

logo_label.image = logo
logo_label.grid(column=1,row=0)

def upload():
    browse.set("loading...")

    path = tk.filedialog.askopenfilename()
    # file = askopenfile(parent=root,mode="rb",title="Choose an image",filetypes =[("JPG file","*.jpg"),("PNG file","*.png"),("JPEG file","*.jpeg"),("All files",".*")])
    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edged)
        #format
        cartoon = Image.fromarray(cartoon)
        cartoon = ImageTk.PhotoImage(cartoon)


        panel = Label(root,image = cartoon)
        panel.grid(column=1, row=3)
        label = tk.Label(image=cartoon)
        label.image = cartoon
        label.grid(row=3, column=1, padx=5, pady=5)





browse = tk.StringVar()
browse_button = tk.Button(root,textvariable = browse,command = lambda:upload(),font = "Raleway",bg="#a022e0",fg ="white",width=15,height =2)

# browse = tk.StringVar()
# browse_button = tk.Button(root,textvariable = browse,command = lambda:upload(),font = "Raleway",bg="#a022e0",fg ="white",width=15,height =2)
browse.set("Browse")
browse_button.grid(column=1,row=2)

canvas = tk.Canvas(root,width = 600,height = 300)
canvas.grid(columnspan = 3)
root.mainloop()







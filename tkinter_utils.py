from tkinter import *

def addSliderTo(label, minValue, maxValue, root):
    label = Label(root, text=label)
    label.pack(side=TOP)

    slider = Scale(root, length=180, from_=minValue, to=maxValue, orient=HORIZONTAL)
    slider.pack(side=TOP)

    return slider

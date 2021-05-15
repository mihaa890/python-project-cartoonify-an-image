
import cv2
from PIL import Image as PILImage, ImageTk
import tkinter as tk
from tkinter import Tk, Frame, Label, BOTTOM, LEFT, RIGHT, TOP, filedialog, NW
import gui

af_img = None

def upload(browse_button_text):
    global image_input
    browse_button_text.set("loading...")

    path = filedialog.askopenfilename()
    if len(path) > 0:
        image_input = cv2.imread(path)
        image_input = cv2.cvtColor(image_input, cv2.COLOR_BGR2RGB)

        # original
        pil_image_original = PILImage.fromarray(image_input)
        tk_image_original = ImageTk.PhotoImage(pil_image_original)

        bf_img = Label(before_image_canvas, width=400, image=tk_image_original)
        bf_img.image = tk_image_original
        bf_img.pack()

def buildImage(props_sliders):
    global af_img

    if(af_img != None):
        af_img = None

    gray = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
    edged = cv2.adaptiveThreshold(gray, props_sliders['thresholdSlider'].get(), cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # cartoonize
    color = cv2.bilateralFilter(image_input, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edged)

    # convert from cv2 to PIL and then to tkImage
    pil_cartoon = PILImage.fromarray(cartoon)
    tk_cartoon = ImageTk.PhotoImage(pil_cartoon)

    af_img = Label(after_image_canvas, width=400, image=tk_cartoon)
    af_img.image = tk_cartoon
    af_img.pack()


def saveimage():
    pass

def drawGUI():
    global before_image_canvas
    global after_image_canvas
    global props_sliders
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # TOP FRAME
    logo = PILImage.open('images/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(topFrame, image=logo)

    logo_label.image = logo
    logo_label.pack()

    browse_button_text = tk.StringVar()
    browse_button = tk.Button(topFrame, textvariable=browse_button_text, command=lambda: upload(browse_button_text), font="Raleway", bg="#a022e0",
                              fg="white", width=15, height=2)

    browse_button_text.set("Browse")
    browse_button.pack()

    #BOTTOM FRAME
    before_image_canvas = tk.Canvas(bottomFrame, width=400, height=600, bg="#9da5a3") #Before
    before_image_canvas.pack(side=LEFT)

    settings_panel = tk.Canvas(bottomFrame, width=400, height=300)  # settings_panel
    settings_panel.pack(side=LEFT)

    after_image_canvas = tk.Canvas(bottomFrame, width=400, height=600, bg="#9da5a3")  # After
    after_image_canvas.pack(side=RIGHT)

    #BUILD_PROPS
    slidersFrame = Frame(settings_panel)
    slidersFrame.pack(side=TOP)

    props_sliders = {
       "thresholdSlider": gui.addSliderTo("Threshold", 0, 255,  slidersFrame)
    }

    #BUILD ACTIONS
    buildActionsFrame = Frame(settings_panel)
    buildActionsFrame.pack(side=BOTTOM)

    build_button = tk.Button(settings_panel, text="BUILD", command=lambda: buildImage(props_sliders),
                              font="Raleway", bg="#a022e0",
                              fg="white", width=20, height=2)

    build_button.pack(side=BOTTOM)

    root.mainloop()

drawGUI()
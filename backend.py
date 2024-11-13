import eel
import tkinter
from tkinter import filedialog
from trace_edge import xy_image, write_img
import os
import matplotlib.pyplot as plt
import numpy as np

eel.init("web")

path = []
height = 0
width = 0
dHeight = 0
dWidth = 0
xy_plotter = None


@eel.expose
def selectFile():
    global path
    global c
    # Initialize tk object
    root = tkinter.Tk()
    # Set always on top for the Tk window
    root.attributes("-topmost", True)
    # Make it dissappear
    root.withdraw()
    # root.iconbitmap('logo_path') or -window_icon = ImageTk.PhotoImage(file="icon.jpg") root.iconphoto(True, window_icon)- to change upload image logo

    # Open file explorer for image upload
    directory_path = filedialog.askopenfile(
        title="Upload Image", filetypes=[("Image Files", "*.png;*.jpeg;*.jpg")]
    )  # return path of file
    if directory_path is not None:
        path = directory_path.name
        return 0
    else:
        return 1


@eel.expose
def setWidth(w):
    global width
    width = w


@eel.expose
def setHeight(h):
    global height
    height = h


@eel.expose
def setDheight(h):
    global dHeight
    print(h)
    dHeight = h
    if dWidth:
        xy_plotter.detect_edge(dHeight, dWidth)


@eel.expose
def setDwidth(w):
    global dWidth
    print(w)
    dWidth = w
    if dHeight:
        xy_plotter.detect_edge(dHeight, dWidth)


@eel.expose
def jsPrint(msg):
    print(msg)


@eel.expose
def writeImg():
    write_img(path)
    return 0


@eel.expose
def trace_edge():
    global xy_plotter
    global path
    xy_plotter = xy_image(30)
    xy_plotter.detect_edge(None, None)
    return 0


@eel.expose
def findPath():
    global path
    if xy_plotter:
        print("finding path")
        path = xy_plotter.findPath()
        print("found path")
        plot()
        return 0
    else:
        print("no image")
        return 1


def removeFiles(w, w1):
    if os.path.isfile("./web/upload_img/img.jpg"):
        os.remove("./web/upload_img/img.jpg")
    if os.path.isfile("./web/export_img/export.jpg"):
        os.remove("./web/export_img/export.jpg")
    exit()


def plot():
    ypoints = np.array([x[0] for x in path])
    xpoints = np.array([x[1] for x in path])
    plt.plot(xpoints, ypoints, ".")
    plt.gca().invert_yaxis()
    plt.show()


eel.start("index.html", size=(500, 500), close_callback=removeFiles)

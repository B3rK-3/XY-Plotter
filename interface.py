import eel
import tkinter
from tkinter import filedialog
from trace_edge import xy_image, write_img
import os

eel.init("web")

path = ""
height = 0
width = 0
xy_plotter = None
path = None

@eel.expose
def selectFolder():
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
def jsPrint(msg):
    print(msg)


@eel.expose
def writeImg():
    write_img(path)


@eel.expose
def trace_edge():
    global xy_plotter
    xy_plotter = xy_image()
    xy_plotter.detect_edge()


@eel.expose
def findPath():
    global path
    path = xy_plotter.findPath()


def removeFiles(w, w1):
    if os.path.isfile("./web/upload_img/img.png"):
        os.remove("./web/upload_img/img.png")
    if os.path.isfile("./web/export_img/export.png"):
        os.remove("./web/export_img/export.png")
    exit()


# Start the index.html file
eel.start("index.html", size=(500, 500), close_callback=removeFiles)

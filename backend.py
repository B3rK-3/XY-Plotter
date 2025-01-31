import eel
from trace_edge import xy_image, write_img
import os
import numpy as np
import tracemalloc



print("imported")
tracemalloc.start()
eel.init("web")

path = []
height = 0
width = 0
dHeight = 0
dWidth = 0
xy_plotter = None

@eel.expose
def postFile(file):
    print(file)

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
def trace_edge(base64IMAGE):
    global xy_plotter
    global path
    xy_plotter = xy_image(30, base64IMAGE)
    return xy_plotter.detect_edge(None, None)


@eel.expose
def findPath():
    global path
    if xy_plotter:
        print("finding path")
        path = xy_plotter.findPath()
        print("found path")
        print(tracemalloc.get_traced_memory())
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


eel.start("index.html", size=(500, 500), close_callback=removeFiles, host='0.0.0.0', port=8080)

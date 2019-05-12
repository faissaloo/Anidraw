#!/usr/bin/env python
# Versions of GIMP below 2.10 will experience memory corruption, do not use them with this plugin
import math
import time
import gtk
from gimpfu import *
from gimpshelf import shelf

def is_img_running(img):
    try:
        return shelf['anidraw_running'][img.ID]
    except KeyError:
        return False

def set_img_running(img, value):
    tmp = shelf['anidraw_running']
    tmp[img.ID] = value
    shelf['anidraw_running'] = tmp

def register_img(img):
    try:
        shelf['anidraw_running']
    except KeyError:
        shelf['anidraw_running'] = {}
    set_img_running(img, True)

def python_anidraw_start(img, drawable, fps=10):
    register_img(img)

    for layer in img.layers:
        layer.visible = False

    prev_layer = None
    while is_img_running(img):
        for layer in img.layers:
            layer.visible = True
            img.active_layer = layer
            if prev_layer:
                prev_layer.visible = False
            drawable.update(0, 0, drawable.width, drawable.height)
            gimp.displays_flush()
            time.sleep(1/fps)
            prev_layer = layer

def python_anidraw_stop(img, drawable):
    if is_img_running(img):
        set_img_running(img, False)
    else:
        gimp.message("Anidraw is not running")

register(
        "python_fu_anidraw_start",
        "Start Anidraw",
        "Start Anidraw",
        "Faissal Bensefia",
        "Faissal Bensefia",
        "2019",
        "<Image>/Image/Anidraw/Start...",
        "RGB*, GRAY*",
        [
                (PF_INT, "FPS", "FPS", 10)
        ],
        [],
        python_anidraw_start)

register(
        "python_fu_anidraw_stop",
        "Stop Anidraw",
        "Stop Anidraw",
        "Faissal Bensefia",
        "Faissal Bensefia",
        "2019",
        "<Image>/Image/Anidraw/Stop",
        "RGB*, GRAY*",
        [],
        [],
        python_anidraw_stop)
main()

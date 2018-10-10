#!/usr/bin/python
# coding: utf8
"""MMM-Selfie - MagicMirror Module
Selfie Script
The MIT License (MIT)

Copyright (c) 2017 Alberto de Tena Rojas (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)
Based on work by Paul-Vincent Roll (Copyright 2016) (MIT License)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import sys
import json
import time
import config
import picamera
import signal
import datetime
import os
import glob
import pygame

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()

# get Picamera or webcam
camera = config.get_camera()

def shutdown():
    to_node("status", 'Shutdown: Cleaning up camera...')
    camera.close()
    quit()

signal.signal(signal.SIGINT, shutdown)

def cleanup():
  to_node("status", 'Cleaning up storage folder of old photos')
  #for fn in glob.iglob(config.path_to_file + '/selfie_' + '*.jpg'):
  #TO DO: if file exists: os.remove("/home/pi/MagicMirror/modules/MMM-Selfie/selfie.jpg")
  to_node("status", 'Removing file ' + "/home/pi/MagicMirror/modules/MMM-Selfie/selfie.jpg")

def takeSelfie():
    pygame.init()
    pygame.mixer.music.load(config.path_to_file + "/../resources/shutter.mp3")
    #filename = config.path_to_file + '/selfie_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
	filename = '/home/pi/MagicMirror/modules/MMM-Selfie/selfie.jpg'
    camera.start_preview()
    time.sleep(3)
    pygame.mixer.music.play()
    camera.capture(filename)
    camera.stop_preview()
    
	to_node("status", 'Selfie taken')
	return filename

# Main Loop
cleanup()
photofile = takeSelfie()
shutdown()

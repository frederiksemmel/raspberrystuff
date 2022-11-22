import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
from gpiozero import Button
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

btn1 = Button(5)                              # assign each button to a variable
btn2 = Button(6)                              # by passing in the pin number
btn3 = Button(13)                             # associated with the button
btn4 = Button(19)  

logging.info("ImagePrinting")   
epd = epd2in7.EPD()

'''2Gray(Black and white) display'''
logging.info("init and Clear")
epd.init()
epd.Clear(0xFF)

def printImage(string):
    logging.info("clear old image")
    epd.Clear(0xFF)
    if(string[:4] != "text"):
        logging.info("read image file")
        Himage = Image.open(os.path.join(libdir, 'images/' + string))
        Himage.resize((176,264))
    else:
        logging.info("writing important message")
        Himage = Image.new('1', (epd.width, epd.height), 255)
        draw = ImageDraw.Draw(Himage)
        if(string == "text"):
            text = 'Frederik'
        else:
            text = 'Marino'
        draw.text((2,0), text)
        draw.text((20,50), 'is Gay')
    epd.display(epd.getbuffer(Himage))



def handleBtnPress(btn):
    
    # get the button pin number
    pinNum = btn.pin.number
    
    # python hack for a switch statement. The number represents the pin number and
    # the value is the message we will print
    switcher = {
        5: "BCG.png",
        6: "qr_wifi.png",
        13: "text",
        19: "text2"
    }
    
    # get the string based on the passed in button and send it to printToDisplay()
    image = switcher.get(pinNum, "Error")
    printImage(image)

btn1.when_pressed = handleBtnPress
btn2.when_pressed = handleBtnPress
btn3.when_pressed = handleBtnPress
btn4.when_pressed = handleBtnPress

logging.info("buttons ready")

while(True):
    time.sleep(100)
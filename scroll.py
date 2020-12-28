import time
from upm import pyupm_jhd1313m1 as lcd
import hashlib
import mraa

LcdWidth = 16
myLcd =lcd.Jhd1313m1(3, 0x3E, 0x62)
myLcd.clear()
myLcd.setColor(0x33, 0x33, 0x33)


led = mraa.Gpio(4)
led.dir(mraa.DIR_OUT)

def getColoursFromText(text):
    """Calculate RGB value from first three bytes of the hash value
    of a string (using SHA-256)
    """
    h = hashlib.sha256()
    h.update(text)
    r, g, b = int(h.hexdigest()[0:2], 16), int(h.hexdigest()[2:4], 16), int(h.hexdigest()[4:6], 16)
    return (r, g, b)

def scrolling(display):
    """ Thread to create scrolling effect """
    i = 0
    n = LcdWidth
    while(True):
        try:
            if bool(display['update']):
                display['update'] = False
                display['led'] = True
                i = 0

                author = display['author']
                if len(author) < LcdWidth:
                    showauthor = author + ":"
                else:
                    showauthor = author[0:(LcdWidth-4)] + "...:"

                myLcd.clear()
                colours = getColoursFromText(author)
                myLcd.setColor(*colours)
                myLcd.setCursor(0, 0)
                myLcd.write(showauthor)
            else:
                text = display['text']
                text_length = len(text)
                if (text_length <= n):
                    showtext = text + " "*(n - text_length)
                    # print(showtext)
                    myLcd.setCursor(1, 0)
                    myLcd.write(showtext)
                else:
                    showtext = text + " "*(n-1)
                    # print(showtext[i:i+n])
                    myLcd.setCursor(1, 0)
                    myLcd.write(showtext[i:i+n])
                    if (i == 0):
                        time.sleep(1)
                    i += 1
                    if (i > text_length):
                        i = 0
                        break
            time.sleep(0.3)
        except IOError:
            time.sleep(0.1)
            pass


import hashlib
from upm import pyupm_jhd1313m1 as lcd
def getColoursFromText(text):
    """Calculate RGB value from first three bytes of the hash value
    of a string (using SHA-256)
    """
    h = hashlib.sha256()
    h.update(text)
    r, g, b = int(h.hexdigest()[0:2], 16), int(h.hexdigest()[2:4], 16), int(h.hexdigest()[4:6], 16)
    return (r, g, b)


def display(message):
    myLcd = lcd.Jhd1313m1(3, 0x3E, 0x62)
    r,g,b=getColoursFromText(message)
    myLcd.setColor(r,g,b)
    myLcd.clear()
    myLcd.write(message)




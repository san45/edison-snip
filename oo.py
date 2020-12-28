import ttt as oled

oled.init()  #initialze SEEED OLED display

oled.clearDisplay()          #clear the screen and set start position to top left corner
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()           #Set addressing mode to Page Mode
for i in range(6):
	oled.setTextXY(i,i)          #Set the cursor to Xth Page, Yth Column  
	oled.putString("Hello World!") #Print the String

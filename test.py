#
# Code to control Intel Edison Bot 
# Free feel to modify, edit and reuse without credits
#

from __future__ import print_function
import time
from upm import pyupm_grovemd as upmGrovemd
from upm import pyupm_jhd1313m1 as lcd
import buzzer
def main():
    I2C_BUS = upmGrovemd.GROVEMD_I2C_BUS
    I2C_ADDR = upmGrovemd.GROVEMD_DEFAULT_I2C_ADDR
    myLcd = lcd.Jhd1313m1(3, 0x3E, 0x62)

    # Instantiate an I2C Grove Motor Driver on I2C bus 0
    myMotorDriver = upmGrovemd.GroveMD(I2C_BUS, I2C_ADDR)
    myLcd.setCursor(0,0)
    # set direction to CW and set speed to 50%
    print("Spin M1 and M2 at half speed for 3 seconds")
    myLcd.setColor(0,100, 0)
    myLcd.write('Going Forward')
    myMotorDriver.setMotorDirections(upmGrovemd.GroveMD.DIR_CCW, upmGrovemd.GroveMD.DIR_CW)
    myMotorDriver.setMotorSpeeds(122, 122)

    time.sleep(10)
    # counter clockwise

    myLcd.setColor(53, 39, 249)
    myLcd.clear()
    myLcd.write('Rotating')
    print("Reversing M1 and M2 for 3 seconds")
    myMotorDriver.setMotorDirections(upmGrovemd.GroveMD.DIR_CW,
    upmGrovemd.GroveMD.DIR_CW)
    buzzer.playGTA()
    buzzer.playGTA()
    time.sleep(5)
    myLcd.clear()
    myLcd.setColor(255,0,0)

    myLcd.write('Halt')
    print("Stopping motors")
    myMotorDriver.setMotorSpeeds(0, 0)

if __name__ == '__main__':
    main()

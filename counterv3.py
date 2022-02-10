from luma.core.interface.serial import pcf8574
from luma.lcd.device import hd44780
from datetime import datetime
import time
interface = pcf8574(address=0x27, backlight_enabled=True)
device = hd44780(interface, width=16, height=2)
device.text = "Hello world"

def vinter():
    now= datetime.now()
    coldday = datetime(year=2022, month=2, day=18, hour=14, minute=15)
    vintercounter= coldday-now
    coldtext = "time until cold"
    coldTime =str(coldday - now)
    device.text = '\n'.join([coldtext, coldTime])
    time.sleep(1)

def end():
    now= datetime.now()
    dayend = now.replace(hour=15,minute=55,second=0)
    timer=dayend - now
    endtext = "time until end"
    endTime =str(dayend - now)
    device.text = '\n'.join([endtext, endTime])
    time.sleep(1)

    


while True:
    vinter()
    end()


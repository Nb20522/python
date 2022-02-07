from luma.core.interface.serial import pcf8574
from luma.lcd.device import hd44780
from datetime import datetime
import time
interface = pcf8574(address=0x27, backlight_enabled=True)
device = hd44780(interface, width=16, height=2)
device.text = "Hello world"


while True:

	now= datetime.now()
	future = now.replace(hour=15,minute=55,second=0)
	time.sleep(1)
	print(future-now)
	device.text = (future-now)

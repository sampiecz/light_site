import asyncio
from kasa import SmartBulb, Discover

class BulbController():

    def __init__(self, bulb_one_name, bulb_two_name):
        bulbs = self.discover_bulbs(bulb_one_name, bulb_two_name)
        self.bulb1 = SmartBulb(bulbs[0])
        self.bulb2 = SmartBulb(bulbs[1])

    def discover_bulbs(self, bulb_one_name, bulb_two_name):
        bulbs = []
        found_devices = asyncio.run(Discover.discover())
        ip_addresses = [item for item in found_devices]
        for count, device in enumerate(found_devices.values()):
            if device.is_bulb:
               bulbs.append(ip_addresses[count]) 
        return bulbs 

    def update_bulbs(self):
        asyncio.run(self.bulb1.update())
        asyncio.run(self.bulb2.update())

    def turn_color(self, hue=255,saturation=100,value=100):
        self.update_bulbs()
        asyncio.run(self.bulb1.set_hsv(hue,saturation,value))
        asyncio.run(self.bulb2.set_hsv(hue,saturation,value))

    def bulb_off(self):
        self.update_bulbs()
        asyncio.run(self.bulb1.turn_off())
        asyncio.run(self.bulb2.turn_off())

    def bulb_on(self):
        self.update_bulbs()
        asyncio.run(self.bulb1.turn_on())
        asyncio.run(self.bulb2.turn_on())

    def turn_blue(self):
        self.bulb_on()
        self.turn_color()

    def turn_red(self):
        self.bulb_on()
        self.turn_color(1,100,100)

"""Bridge pattern explanation. Abstraction"""
import samsung_tv
import lg_tv

class TV:
    """Here is an abstraction of some TV"""
    def __init__(self, tv):
        self.tv = tv()

    def power_on(self):
        print('Power on TV')
        self.tv.power_on()

    def power_off(self):
        print('Power off TV')
        self.tv.power_off()

    def volume_up(self):
        print('Volume up')
        self.tv.increase_volume()

    def volume_down(self):
        print('Volume down')
        self.tv.decrease_volume()

    def chanel_up(self):
        print('Channel up')
        self.tv.next_channel()

    def chanel_down(self):
        print('Channel down')
        self.tv.prev_channel()

# Client choose TV type
client_tv = TV(samsung_tv.UE55NU7090UXUA)

client_tv.power_on()
client_tv.chanel_up()
client_tv.chanel_up()
client_tv.chanel_down()
client_tv.volume_up()
client_tv.volume_up()
client_tv.power_off()


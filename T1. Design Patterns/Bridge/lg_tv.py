"""Bridge pattern explanation. Realization"""


class LG43UM7100PLB:
    WELLCOME_MSG = "LG Smart TV"
    CURRENT_CHANNEL = 1

    """Here is a realization of LG TV"""

    def __init__(self):
        self.load_tv_description()
        self.prev_ch = 0

    def power_on(self):
        """ Specific power on action for LG tv"""
        # self.LGF1Reley.on()
        # self.XCF17Reley.on()
        # self.start_bootloader()
        pass

    def power_off(self):
        """ Specific power off action for Samsung tv"""
        # self.stop_bootloader()
        # self.XCF17Reley.off()
        # self.LGF1Reley.off()
        pass

    def increase_volume(self):
        # volume = self.get_volume()
        # self.change_volume(volume + 1)
        # self.show_volume_image(self.get_volume())
        pass

    def decrease_volume(self):
        # volume = self.get_volume()
        # self.change_volume(volume - 1)
        # self.show_image(self.get_volume())
        pass

    def next_channel(self):
        """Similar to increase volume"""
        # self.prev_ch = self.CURRENT_CHANNEL
        # self.CURRENT_CHANNEL = + 1
        # self.show_img(self.CURRENT_CHANNEL)
        pass

    def prev_channel(self):
        """Similar to decrease volume"""
        # self.CURRENT_CHANNEL = self.prev_channel
        # self.prev_ch = self.CURRENT_CHANNEL - 1
        # self.show_img(self.CURRENT_CHANNEL)
        pass

    def load_tv_description(self):
        """Set tv description"""
        pass

"""Bridge pattern explanation. Realization"""


class UE55NU7090UXUA:
    WELLCOME_MSG = "Samsung Smart TV"
    CURRENT_CHANNEL = 1

    """Here is a realization of Samsung TV UE55NU7090UXUA model"""

    def __init__(self):
        self.prev_ch = 0

    def power_on(self):
        """ Specific power on action for Samsung tv"""
        # self.CXF15Reley.on()
        # self.DCF1Reley.on()
        # self.mount_image()
        pass

    def power_off(self):
        """ Specific power off action for Samsung tv"""
        # self.unmount_image()
        # self.DCF1Reley.off()
        # self.CXF15Reley.off()
        pass

    def increase_volume(self):
        # volume = self.get_volume()
        # self.change_volume(volume + 1)
        # self.show_volume_image()
        pass

    def decrease_volume(self):
        # volume = self.get_volume()
        # self.change_volume(volume - 1)
        # self.show_volume_image()
        pass

    def next_channel(self):
        """Similar to increase volume"""
        # self.prev_ch = self.CURRENT_CHANNEL
        # self.CURRENT_CHANNEL = + 1
        # self.show_channel_img(self.CURRENT_CHANNEL)
        pass

    def prev_channel(self):
        """Similar to decrease volume"""
        # self.CURRENT_CHANNEL = self.prev_channel
        # self.prev_ch = self.CURRENT_CHANNEL - 1
        # self.show_channel_img(self.CURRENT_CHANNEL)
        pass


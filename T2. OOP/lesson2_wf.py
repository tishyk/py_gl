"""
Add session 2 test data
"""

class Client:
    def __init__(self, ip, client_type):
        enabled = False  # Uppercase
        self.ip = ip
        self.client_type = client_type


class Server:
    def __init__(self, ip):
        self.static_ip = ip
        self.clients = []
        self.active_clients = []

    def skip_mac(self):
        """ Disable all mac clients """
        pass

    def power_reset(self):
        print('Server power reset')

if __name__ == "__main__":
    server = Server("192.168.1.200")

    client1 = Client("192.168.1.100", 'Mac')
    client2 = Client("192.168.1.101", 'Win')
    client3 = Client("192.168.1.102", 'Linux')




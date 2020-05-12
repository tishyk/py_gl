"""
First session
"""

KNOWN_CLIENTS = ("192.168.1.201", "00-11-22-33-44-55", "192.168.1.202")


class Client:
    allowed_servers = []

    def __init__(self, ip, client_type):
        enabled = False  # Uppercase
        self.ip = ip
        self.client_type = client_type

    @classmethod
    def wake_up(cls, client_id):
        x = cls.allowed_servers
        # Client enabled by server if last in allowed server list
        # Client OS started, client ip received
        print("StaticMethod", x, client_id)
        return True

    @staticmethod
    def ping(ip):
        print(ip)

    def power_off(self):
        # Power off client method
        # Client ip released
        pass

    def new_mac_client(self):
        # New Mac client object creation
        pass


client1 = Client('test3', 'win')
client1.ping(ip='test_ip')


class Server:
    """ Server desc"""
    POWER_ON = True

    def __init__(self, ip, state=False):
        self.static_ip = ip
        self.available_clients = []
        self.POWER_ON = state


    def wake_up(self):
        """ Enable server
        # Start all known clients"""
        print("Server method")
        self.x = self.y + 10
        pass

    def power_reset(self):
        print('Server power reset')

    def client_wake_up(self):
        for client in KNOWN_CLIENTS:
            Client.wake_up(client)


class CS(Client, Server):
    def __init__(self):
        self.y = 50

    def wake_up(self):
        """ Enable server and clients
        # Start all known servers and clients"""
        """ Enable server
        # Start all known clients"""
        print("CS method")
        super().wake_up('Client')
        super(Client, self).wake_up()   # Wake up server



if __name__ == "__main__":
    server1 = Server("192.168.1.100", True)
    server2 = Server("192.168.1.101", True)
    server3 = Server("192.168.1.102")
    cs = CS()
    cs.wake_up()




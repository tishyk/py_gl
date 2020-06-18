"""
First session
"""

KNOWN_CLIENTS = ("192.168.1.201", "00-11-22-33-44-55", "192.168.1.202")
client1, *unn_var = KNOWN_CLIENTS

class BaseServer():
    def wake_up(self):
        """ Enable server
        # Start all known clients"""
        print("Server method")
        self.__class__.D_IP = "192.168.0.1"
        pass


class Server(BaseServer):
    """ Server desc"""
    POWER_ON = True
    DEFAULT_IP = '127.0.0.1'

    def __init__(self, ip, state=False, *args, **kwargs):
        self.static_ip = ip
        self.available_clients = []
        self.POWER_ON = state
        self.known_clients = kwargs.get('known_clients')
        if kwargs.get('y'):
            client = True

    def power_reset(self):
        print('Server power reset')

    def client_wake_up(self):
        for client in KNOWN_CLIENTS:
            Client.wake_up(client)


class Client:
    DEFAULT_IP = []
    allowed_servers = [None]

    def __init__(self, ip, client_type):
        enabled = False  # Uppercase
        self.ip = ip
        self.client_type = client_type

    def wake_up(self, client_id):
        x = self.allowed_servers
        # Client enabled by server if last in allowed server list
        # Client OS started, client ip received
        print("Client Method", x, client_id)
        return True

    def ping(self, ip):
        print(ip)

    def power_off(self):
        # Power off client method
        # Client ip released
        pass


class CS(Client, Server, object):
    DEFAULT_IP= ''
    def __init__(self):
        self.y = 50

    def wake_up(self):
        """ Enable server and clients
        # Start all known servers and clients"""
        """ Enable server
        # Start all known clients"""
        print("CS method")
        super().wake_up('Client')
        super(Client, self).wake_up()  # Wake up server


if __name__ == "__main__":
    server = Server("192.168.1.100", True)
    cs = CS()
    cs.wake_up()


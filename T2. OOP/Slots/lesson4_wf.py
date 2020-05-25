"""
First session
"""
import copy

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

    def __init__(self, state=False, **kwargs):
        self.available_clients = []
        self.POWER_ON = state
        self.result = False
        self.__dict__.update(kwargs)

    def clone(self, ip):
        new_server = copy.deepcopy(self)
        new_server.ip = ip
        self.available_clients = []
        return new_server

    def run(self):
        print(self.ip, self.available_clients)
        self.result = True


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
        super(Client, self).wake_up()  # Wake up server


if __name__ == "__main__":
    server = Server(state=True)
    server.available_clients = ['1', 2, 3]
    server_lst = ["192.168.1.100", "192.168.1.101", "192.168.1.103"]

    for server_ip in server_lst:
        last_server = server
        new_server = server.clone(server_ip)
        if last_server.result:
            new_server.run()
        else:

        server.run()

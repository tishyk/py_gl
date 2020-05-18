"""
Session 2
"""

import gc
import json
from weakref import WeakValueDictionary


class Client:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, ip, client_type, **kwargs):
        self.enabled = False
        self.ip = ip
        self.client_type = client_type

    def run(self):
        print(f'Run {self.ip}')

    def __repr__(self):
        return f"{self.ip} {self.__class__.__name__}"

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.ip == other.ip


class Server:

    def __init__(self, ip, **kwargs):
        self.static_ip = ip
        self.clients = []
        self.active_clients = []
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} {self.static_ip};\n Active clients: {self.active_clients}"

    def __len__(self):
        return len(self.active_clients)

    def __add__(self, other):
        assert isinstance(other, Client)
        self.active_clients.append(other)
        return self

    def __iter__(self):
        return iter(self.active_clients)

    def __enter__(self):
        self.power_reset()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active_clients = []

    def __getattr__(self, item):  # for not implemented attributes only
        print('Get attr {}'.format(item))
        return 'Not implemented Warning'

    def __setattr__(self, item, value):  # for not implemented attributes only
        self.__dict__[item] = value
        return 'not implemented'

    def __getattribute__(self, item):  # for all implemented attributes
        print("Get attribute: {}".format(item))
        return super().__getattribute__(item)

    def skip_mac(self):
        """ Disable all mac clients """
        print("Skip Mac")
        pass

    def power_reset(self):
        print('Server power reset')


if __name__ == "__main__":
    server = Server("192.168.1.200", **json.load(open('Meta class/event_default.json')))

    client1 = Client("192.168.1.100", 'Mac', server=server)
    client2 = Client("192.168.1.101", 'Win', server=server)
    client3 = Client("192.168.1.102", 'Linux', server=server)
    client4 = Client("192.168.1.102", 'Linux', server=server)

    print(server.clients)

    for win_client in server.win_clients:
        win_client.run()

    with Server("192.168.1.201") as server2:
        server2.skip_mac()

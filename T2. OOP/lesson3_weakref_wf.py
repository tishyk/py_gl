"""
Session 3
"""

import gc
import json
from weakref import WeakValueDictionary


class Client:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, ip, client_type, **kwargs):
        self.__dict__.update(kwargs)
        self.enabled = False
        self.ip = ip
        self.client_type = client_type

    def ready(self):
        return True

    def run(self):
        print(f'Run {self.ip}')

    def __repr__(self):
        return f"{self.ip} {self.__class__.__name__}"

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.ip == other.ip


class Server:

    def __init__(self, ip, **kwargs):
        self.__dict__.update(kwargs)
        self.static_ip = ip
        self.active_clients = {}
        self.weak_active_clients = WeakValueDictionary()

    def __str__(self):
        return f"{self.__class__.__name__} {self.static_ip};\n Active clients: {self.active_clients}"

    def __len__(self):
        return len(self.active_clients)

    def add_client(self, *clients):
        """ Add client to server active clients """
        for client in clients:
            self.active_clients[client.ip] = client

    def add_weak_client(self, *clients):
        """ Client will be used for one action only.
         No need to store this client objects in memory till the end of main script execution.
         Client object will be deleted manually after some concrete usage."""
        for client in clients:
            self.weak_active_clients[client.ip] = client
        pass


if __name__ == "__main__":
    server = Server("192.168.1.200", **json.load(open('Meta class/event_default.json')))

    client_m1 = Client("192.168.1.100", 'Mac')
    client_l1 = Client("192.168.1.102", 'Linux')
    server.add_client(client_m1, client_l1)

    for client in server.active_clients.values():
        client.run()

    del client_m1
    del client_l1

    client_m2 = Client("192.168.1.101", 'Mac')
    client_l2 = Client("192.168.1.103", 'Linux')
    server.add_weak_client(client_m2, client_l2)

    print('\n***', len(server.active_clients), len(server.weak_active_clients))
    for client in server.weak_active_clients.values():
        client.run()

    del client_m2
    del client_l2
    gc.collect()


    for client in server.active_clients.values():
        client.run()

    for client in server.weak_active_clients.values():
        client.run()

    print('\n***', len(server.active_clients), len(server.weak_active_clients))
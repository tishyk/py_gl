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
        self.enabled = True
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


class IP_Descriptor():
    def __init__(self, name):
        self.ip_variable = name

    def __get__(self, instance, cls):
        """ instance: instance being manipulated. Ex. Client instance"""
        if instance.enabled:
            print("IP address: {}".format(instance.__dict__[self.ip_variable]))
        else:
            raise RuntimeError('Host disabled. Failed to get ip')
        return instance.__dict__[self.ip_variable]

    def __set__(self, instance, value):
        if not instance.enabled:
            raise RuntimeError("Could not set ip address for disabled host")
        else:
            assert isinstance(value, str), "It is not possible to set ip address as int object"
            assert len(value.split('.')) == 4, "Invalid string value for ip address"
            instance.__dict__[self.ip_variable] = value


def __delete__(self, instance):
    print(f"Delete: {instance.__name__}")
    del instance.__dict__[self.ip_variable]


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

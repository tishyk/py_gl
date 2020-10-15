class Person:
    """Docstring"""
    my_age = 24 # class variable

    def __init__(self, first, last, age, *args, **kwargs):
        """Funcstring""" # __doc__
        self.first = first # object variable
        self.last = last # object variable
        self.age = age
        self.args = args
        self.kwargs = kwargs
        self.__strong = 100
        self.domain = "gmail.com"

    @property
    def email(self, domain="hotmail.com"):
        return "{}.{}@{}".format(self.first, self.last, domain)

    @email.setter
    def email(self, value):
        f_l, self.domain = value.split('@')
        self.first, self.last = f_l.split('.')

    @email.deleter
    def email(self):
        self.last = ''

class Child(Person):
    @property
    def email(self):
        super().email
        return "Hi"

John = Person('John', "Smith", 35)
John.email
John.email = "John.Doe@hotmail.com"
pass

#
# # Application Connections
#
# import getpass
# # from app_abstractions import ABCConnection
# from app_descriptors import IP_Descriptor
# import copy
#
# class Serial():
#     pass
#
# class Serial232():
#     pass
#
# class Telnet():
#     pass
#
# class AppServer():
#     pass
#
# class FTP():
#     pass
#
# class SSH():
#     #address = IP_Descriptor('address')
#
#     def __new__(cls, *args, **kwargs):
#         print("SSH connection")
#         return super().__new__(cls)
#
#     def __init__(self, *args, **kwargs):
#         # super().__init__(*args, **kwargs)
#         self.rank = 10
#
#     def __call__(self, cmd):
#         print(f"Execute command: {cmd}")
#         return "cmd_output"
#
#     def __del__(self):
#         del self.rank
#
#     def __str__(self):
#         return self.__class__.__name__
#
#     def __eq__(self, test_obj):
#         return self.rank == test_obj
#
#     def __round__(self):
#         return self.rank
#
#     def __add__(self, other):
#         new_obj = copy.deepcopy(self)
#         new_obj.rank = new_obj.rank + other.rank
#         return new_obj
#
#     def __int__(self):
#         return self.rank
#
#     def __getattr__(self, item):  # for not implemented attributes only
#         print('Get attr {}'.format(item))
#         return 'not implemented'
#
#     def __setattr__(self, item, value):  # for not implemented attributes only
#         self.__dict__[item] = value
#
#     def __getattribute__(self, item):
#         if item == 'rank':
#             return 20
#         print("Get attribute: {}".format(item))
#         return super().__getattribute__(item)
#
#
#     def call(self, cmd):
#         # connection call method realization
#         pass
#
#     def check_call(self, cmd, timeout=60):
#         # connection call method realization
#         pass
#
#     def check_output(self, cmd, timeout=60):
#         # connection call method realization
#         pass
#
#     def connect(self):
#         # Connection via supported connection type
#         #password = getpass.getpass()
#         # create connection to host
#         self.connected = True
#
#     def close_connection(self):
#         # Close supported connection type
#         pass
#
#     def wait_for_connection(self, timeout, polling=0.1):
#         # connection call method realization
#         pass
#
#     def is_alive(cls):
#         # check connection created and is alive
#         pass
#
# if __name__ == "__main__":
#     # For ssh object testing
#     ssh1 = SSH('10.124.198.24')
#     # ssh2 = SSH('10.124.198.24')
#     # if callable(ssh1):
#     #     ssh1('ping')
#     #
#     # # if ssh1 == 10:
#     # #     ssh1('cmd')
#     #
#     # x = round(ssh1)
#     # ssh3 = ssh1 + ssh2
#     # y = int(ssh1)
#
#
#     # del ssh
#     pass

class Adapter:
    def run():
        pass


class Object(object):
    var = 10


    def run(self):
        print("Run")


o = Object()


o.run()


class ProxyObject(object):
    def __init__(self):
        self.o = Object()

    var = 10
    def run(self):
        print('actions')
        self.o.run()

pass


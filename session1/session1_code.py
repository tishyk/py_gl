thisdict = {
    "model": "Mustang",
    "year": 1964
}

cars = [1, "Ford", "Volvo", "BMW"]


def func(x, y, z=0, *args, **kwargs):
    if kwargs.get('brand', '') == 'Ford':
        print("Get Ford auto")
    print(x, y, z, type(args), type(kwargs), args, kwargs)

class BaseParams:
    """Base param class"""
    def run(self, x):
        print(self.__class__.__doc__, x)

    def clear(self, x):
        del x

    def need_run(self):
        print("Hi")


class A:
    def need_run(self):
        print("Hello")

class Params(BaseParams, A):
    """Params param class"""
    BRAND = "Fiat"
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        if kwargs.get('BRAND'):
            cls.BRAND = kwargs.get('BRAND')
        obj.__dict__.update(kwargs)
        return object.__new__(cls)

    def __init__(self, x, y, z=0, *args, **kwargs):
        self.x = x
        self.y = y
        self.__dict__.update(kwargs)
        d1 = self.__class__.__dict__
        d2 = Params.__dict__
        # if kwargs.get('brand', '') == 'Ford':
        #     print("Get Ford auto")
        print(x, y, z, type(args), type(kwargs), args, kwargs)

    def run(self):
        self.__class__.set = ""
        super().run(self.x)
        super().clear(self.x)
        super().need_run()




    @classmethod
    def brand_clear(cls):
        cls.BRAND = ""

    @staticmethod
    def create_zparam(x, z, y=0):
        return Params(x, y, z)


# func(10, 15, 1, "Ford", "Volvo", "BMW")
# param = Params(10, 15, 1, "Ford", "Volvo", "BMW")

# func(10, 15, *cars)
# param = Params(10, 15, *cars)

# func(10, 15, *cars, brand="Ford", model="Mustang", year=1964)
# param = Params(10, 15, *cars, brand="Ford", model="Mustang", year=1964)
#
# func(10, 15, *cars, **thisdict)
# param1 = Params(10, 15, *cars, **thisdict)
# param2 = Params(10, 15, *cars, **thisdict)
# param3 = Params(10, 15, *cars, **thisdict)
# # xy = param.x + param.y + param.brand
#
#
#
# param
# <__main__.Params object at 0x0305FE30>
# param.__dict__
# {'x': 10, 'y': 15}
# param.__dict__['y']
# 15
# Params.__dict__
# mappingproxy({'__module__': '__main__', '__init__': <function Params.__init__ at 0x030E0660>, '__dict__': <attribute '__dict__' of 'Params' objects>, '__weakref__': <attribute '__weakref__' of 'Params' objects>, '__doc__': None})
# import pprint
# pprint.pprint(Params.__dict__)
# mappingproxy({'__dict__': <attribute '__dict__' of 'Params' objects>,
#               '__doc__': None,
#               '__init__': <function Params.__init__ at 0x030E0660>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'Params' objects>})
# param.__dict__['brand'] = "Ford"
# param.x
# 10
# param.brand
# 'Ford'
# """
param1 = Params(10, 15, *cars, **thisdict)
param1.BRAND = 10
param1.run()

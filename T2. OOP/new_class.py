class ClassObj(type):
    class_var = 20

    def __new__(cls, cls_name, bases, clsdict):
        print(f"Class {cls_name} creation")
        if len(bases) < 1:
            raise TypeError(f"Can't instantiate abstract class {cls_name}")
        clsobj = super().__new__(cls, cls_name, bases, clsdict)
        return clsobj

    def go(cls):
        print("Go")

class Object(metaclass=ClassObj):
    obj_var = 10

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def run(self):
        print("Run")



o = Object()
o.run()

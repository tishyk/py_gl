import json


def loader():
    json_dict_file = open("uz_bukovel_event.json", 'r', encoding='utf8')
    json_dict = json.loads(json_dict_file.read())
    return json_dict


class MyType(type):
    def __new__(cls, class_name, bases, clsdict):
        clsdict.update(loader())
        cls_obj = super().__new__(cls, class_name, bases, clsdict)
        #cls_obj = super().__new__(cls, class_name, bases, loader() )
        return cls_obj


class Event(metaclass=MyType):
    data = 10


event1 = Event()
event2 = Event()
event3 = Event()
pass  # Debug it from here

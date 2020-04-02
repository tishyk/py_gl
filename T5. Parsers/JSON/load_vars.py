import json

class DataLoader():
    Config_Path1 = 'data_files.json'
    def __init__(self):
        self.__dict__.update(self.load(self.Config_Path1))

    def load(self, path):
        py_dict = {}
        py_array = json.load(open(path, encoding='utf8'))
        for item in py_array:
            if type(item) is dict:
                py_dict = item
                break
        return  py_dict

data = DataLoader()
print(data.lastName)
import json
from unittest.mock import Mock

# JavaScript Object Notation was inspired by a subset of the
# JavaScript programming language dealing with object literal syntax.

# JSON supports primitive types, like strings and numbers, as well as nested lists and objects.
JSON_DATA = """[10, 20,
    "hello", {
    "firstName": "Jane", 
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}]"""
# Serialize in a one
json = Mock(name="Hi")

python_object = json.loads(JSON_DATA)
python_object2 = json.loads("kzdjbjdb")
python_object2 = json.loads(151515148)
json.loads.assert_called()
json.loads.name = "Mock name"
print(json.loads.call_count)

print(python_object)
# json.dump(python_object,open('data_files.json', 'w'), indent=4)
#
#
# """
# Python	            JSON
# dict	            object
# list, tuple 	    array
# str	                string
# int, long, float	number
# True	            true
# False	            false
# None	            null
# """
#
# # Imagine you’re working with a Python object in memory that looks a little something like this:
#
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
# with open("data_file.json", "w") as write_file:
#     # dump() takes two positional arguments:
#     # (1) the data object to be serialized, and
#     # (2) the file-like object to which the bytes will be written
#     json.dump(data, write_file)
#
#
#
#
# # Deserializing JSON
# blackjack_hand = (8, "Q")
# encoded_hand = json.dumps(blackjack_hand)
# decoded_hand = json.loads(encoded_hand)
#
# blackjack_hand == decoded_hand          # --> False
# type(blackjack_hand)                    # ---> <class 'tuple'>
# type(decoded_hand)                      # --> <class 'list'>
# blackjack_hand == tuple(decoded_hand)   # --> True
#
#
# with open("data_file.json", "r") as read_file:
#     # read from a file object( file/socket/stream/PIPE)
#     data = json.load(read_file)
# # In most cases, the root object will be a dict or a list
#
#

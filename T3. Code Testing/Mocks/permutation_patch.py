import itertools
from unittest.mock import patch

name = 'достаточно длинное имя'


def real(name):
    if len(name) < 10:
        raise ValueError('String too short to calculate statistics.')
    y = 0
    for i in itertools.permutations(range(len(name)), 10):
        y += sum(i)
        print(y, i)


with patch('itertools.permutations') as perm_mock:
    perm_mock.return_value = [(10, 12, 14), (12, 14, 10)]
    real(name)
    perm_mock.assert_called_with(range(len(name)), 10)
    pass

# 	called — вызывался ли объект вообще
# 	call_count — количество вызовов
# 	call_args — аргументы последнего вызова
# 	call_args_list — список всех аргументов
# 	method_calls — аргументы обращений к вложенным методам и атрибутам (о них — ниже)
# 	mock_calls — то же самое, но вместе и для самого объекта, и для вложенных
# assert_not_called
# assert_has_calls

import itertools

name = 'достаточно длинное имя'


def real(name):
    if len(name) < 10:
        raise ValueError('String too short to calculate statistics.')
    y = 0
    for i in itertools.permutations(range(len(name)), 10):
        y += sum(i)
        print(y, i)


real(name)

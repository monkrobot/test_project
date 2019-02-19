class Adder():
    def __init__(self, data):
        self.data = data

    def add(self, x, y):
        return 'Not Implemented'

    def __add__(self, other):
        return self.add(self.data, other)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        return dict(x, **y)


a = Adder([1, 2, 3])
# a.add(5, 7)
print(a + 5)

b = ListAdder([1, 2, 3])
# print(b.add([1, 2, 3], [9, 8, 7]))
print(b + [9, 8, 7])

c = DictAdder({'a': 1, 'b': 2})
# print(c.add({'a': 1, 'b': 2}, {'c': 9, 'd': 10}))
print(c + {'c': 9, 'd': 10})

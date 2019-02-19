class MyList:
    def __init__(self, data):
        self.data = []
        for x in data:
            self.data.append(x)

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        #return self.__add__(other)
        return other + self.data

    def __getitem__(self, item):
        return self.data[item]

    def append(self, other):
        return self.data.append(other)

    def __iter__(self):
        for i in self.data:
            yield i

    def __delitem__(self, key):
        return self.data.pop(key)

    def sort(self, rev=True):
        if rev:
            return sorted(self.data)
        else:
            return sorted(self.data, reverse=True)

    def __repr__(self):
        return repr(self.data)


if __name__ == "__main__":
    a = MyList([4, 6, 2, 5, 9])
    #print(a.sort(False))
    #for k in a:
    #    print(k)
    #
    #print(a[2])
    #print(a[1:3])
    #
    #a.append(4)
    #print(a)
    #
    #print(a.sort(False))
    #
    #print(a)

    #print(a)
    #del a[1]
    #print('This: ', a)
    #del a[1]
    #print('This: ', a)

    a + [4, 5, 6]
    print(a)

    print(a + [4, 5, 6])
    print(a)

    a + [4, 5, 6]
    print(a)



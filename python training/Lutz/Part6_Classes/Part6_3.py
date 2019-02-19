from Part6_2 import MyList


class MyListSub(MyList):
    Count = 0
    stdout_c = 0

    def __getattribute__(self, item):
        print('Message: Attribute is ', item)
        return object.__getattribute__(self, item)

    def __add__(self, other):
        self.Count += 1
        return super().__add__(other)

    def __repr__(self):
        self.stdout_c += 1
        return super().__repr__()


if __name__ == "__main__":
    b = MyListSub([1, 2, 3])
    print(b)
    #print(b.Count)
    #print(b.stdout_c)
    #print('c')
    #c = MyListSub([4, 5, 6])
    #print(c)
    #print(c.Count)
    #print(c.stdout_c)


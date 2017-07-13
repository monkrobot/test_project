class MyList:
    def __init__(self, somelist):
        self.mylist = []
        for x in somelist: self.mylist.append(x)

    def __add__(self, other):
        return self.mylist + other

    def __getitem__(self, item):
        return self.mylist.__getitem__(item)

    def append(self, item):
        self.mylist.append(item)
        return self.mylist


class MyListSub(MyList):
    count = 0
    def __init__(self):
        MyList.__init__()
        MyListSub.count = MyListSub.count + 1

    def printCount(self):
        print('count is: ', MyListSub.count)

m = MyList([1,2,3,4,5])
print(m[2:4])
print(m + [1])

print(m.append(15))

k = MyList([1,2,3,4,5])
d = MyList([1,2,3,4,5])
f = MyListSub([1,2,3,4,5])
f.printCount()

print(f + [1])
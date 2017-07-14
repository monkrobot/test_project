class Testclass:
    def __init__(self, myset):
        #self.myset = set(myset)
        self.myset = myset

    def __and__(self, other):
        if type(other) == set:
            return self.myset.intersection(other)

    def __or__(self, other):
        if type(other) == set:
            return self.myset.union(other)

    def __str__(self):
        return str(self.myset)

    def __getitem__(self, item):
        return self.myset[item]

    def __iter__(self):
        return self

    #def __next__(self):
    #    if self.value == self.stop:
    #        raise StopIteration
    #    self.value += 1
    #    return self.value ** 2


#setA = Testclass('asdbc')
setA = Testclass([1,3,5])
setB = {'a','b','c','1'}

#print(setA & setB)


print('lsjdg')
for i in setA:
    print(i, end=' ')
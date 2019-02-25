# from Part6_2 import MyList


class Meta:  # (MyList):
    # def __getattr__(self, item):
    #     print('get', item)
    def __getattribute__(self, item):
        try:
            # print('attributes: ', super().__getattribute__(item).__code__.co_varnames)
            print('attributes: ', object.__getattribute__(self, item).__code__.co_varnames)
        except AttributeError:
            print(item)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('set', key, value)
        object.__setattr__(self, key, value)

    def test(self, k=1, f=0):
        return k+f


if __name__ == "__main__":
    a = Meta() # [1, 2, 3])
    print(a.test())
    print("a.pay")
    a.pay = 10
    print(a.pay)

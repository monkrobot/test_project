def test(k=1, f=0):
    return k + f

print(test.__dict__)


class Meta:

    def __getattribute__(self, item):
        print("Catch method")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def test(self, k=1, f=0):
        return k+f


if __name__ == "__main__":
    a = Meta()
    print(a.test())
    a.pay = 10
    print(a.pay)


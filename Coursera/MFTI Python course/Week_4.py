class ForItem:
    def __init__(self, list_item):
        self.list_item = list_item

    def __getitem__(self, item):
        return self.list_item[item]

    def __setitem__(self, key, value):
        self.list_item[key] = value

    def __str__(self):
        return self.list_item.__str__()


a = [9,8,7,6,5]
foritem = ForItem(a)
print(foritem[3])

foritem[3]=43
print(foritem[3])

print(foritem)
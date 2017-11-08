#class ForItem:
#    def __init__(self, list_item):
#        self.list_item = list_item
#
#    def __getitem__(self, item):
#        return self.list_item[item]
#
#    def __setitem__(self, key, value):
#        self.list_item[key] = value
#
#    def __str__(self):
#        return self.list_item.__str__()
#
#
#a = [9,8,7,6,5]
#foritem = ForItem(a)
#print(foritem[3])
#
#foritem[3]=43
#print(foritem[3])
#
#print(foritem)

import time

class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("Elapsed: {}".format(self.current_time()))

with timer() as t:
    time.sleep(1)
    print("Current: {}".format(t.current_time()))
    time.sleep(1)
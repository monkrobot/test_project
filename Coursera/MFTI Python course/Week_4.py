#Exercise 1
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


#Exercise 2
#import time
#
#class timer():
#    def __init__(self):
#        self.start = time.time()
#
#    def current_time(self):
#        return time.time() - self.start
#
#    def __enter__(self):
#        return self
#
#    def __exit__(self, *args):
#        print("Elapsed: {}".format(self.current_time()))
#
#with timer() as t:
#    time.sleep(1)
#    print("Current: {}".format(t.current_time()))
#    time.sleep(1)


##Programming exercise (Особые методы классов)
#import tempfile
#
#class File:
#    def __init__(self, path):
#        self.path = path
#        #self.file = open(path, 'w+')
#        #self.read = self.file.read()
#        #self.lines = self.file.readlines()
#        self.current = 0
#
#    def write(self, information):
#        with open(self.path, 'a') as file:
#            return file.write(information)
#
#    def __add__(self, other):
#        file = open(self.path)
#        file2 = open(other.path)
#        first = bytes(file.read(), encoding='utf-8')
#        second = bytes(file2.read(), encoding='utf-8')
#        #print('self.file.read()', first)
#        #print('first', first)
#        new_file = tempfile.TemporaryFile()
#        new_file.write(first)
#        new_file.write(second)
#        new_file.seek(0)
#        #print('new_file', new_file.read())
#        file.close()
#        file2.close()
#        return new_file
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        with open(self.path) as file:
#            lines = file.readlines()
#            if self.current >= len(lines):
#                raise StopIteration
#
#            result = lines[self.current]
#            self.current += 1
#            return result
#
#    def __str__(self):
#        return self.path
#
#    #def __exit__(self, *args):
#    #    self.file.close()
#
#obj = File("testingWeek4.txt")
#print('obj', obj)
#
##obj.write("hello everybody3\n")
#for line in obj:
#    print('This is line:', line)
#
#obj.write("New string")
#
#result_obj1 = File("testingWeek4.txt")
#
#result = obj + result_obj1
##result.seek(0)
#print("Result of +:", result.read())


#Descriptors

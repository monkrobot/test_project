import shelve

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bod Smith','None',100)
sue = Person('Sue Jones','prg',10000)
tom = Person('Tom Hardi','mrg',20000)

file_db = shelve.open('persondb')
for object in (bob, sue, tom):
    file_db[object.name] = object
file_db.close()
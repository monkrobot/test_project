import shelve

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def __str__(self):
        return str(self.lastName()) + " " + str(self.job) + " " + str(self.pay)

bob = Person('Bod Smith','None',100)
sue = Person('Sue Jones','prg',10000)
tom = Person('Tom Hardi','mrg',20000)
#print(sue)

file_db = shelve.open('persondb')
for object in (bob, sue, tom):
    file_db[object.name] = object
file_db.close()
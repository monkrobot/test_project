class Actor:
    def line(self):
        print(self.name +':', str(self.says()))

class Scene:
    def __init__(self):
        self.cust = Customer()
        self.clerk = Clerk()
        self.par = Parrot()

    def action(self):
        self.cust.line()
        self.clerk.line()
        self.par.line()

class Customer(Actor):
    name = 'cust'
    def says(self):
        return("Customer")

class Clerk(Actor):
    name = 'Cle'
    def says(self):
        return("Clerk")

class Parrot(Actor):
    name = 'Par'
    def says(self):
        return ("Parrot")

Scene().action()
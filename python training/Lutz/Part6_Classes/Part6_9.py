## My solution - Not bad, but not good
#class Scene:
#    def action(self):
#        customer = Customer()
#        clerk = Clerk()
#        parrot = Parrot()
#
#        for k in [customer, clerk, parrot]:
#            print(k.__class__.__name__ + ': ' + str(k.line()))
#
#
#
#class Customer:
#    def line(self):
#        return("Customer")
#
#
#class Clerk:
#    def line(self):
#        return("Clerk")
#
#
#class Parrot:
#    def line(self):
#        return("Parrot")
#
#
#parrot = Scene()
#parrot.action()


class Actor:
    def line(self):
        print(self.name + ': ' + self.says())


class Customer(Actor):
    name = "Customer"

    def says(self):
        return "no Customer"


class Clerk(Actor):
    name = "Clerk"

    def says(self):
        return "no Clerk"


class Parrot(Actor):
    name = "Parrot"

    def says(self):
        return "no Parrot"


class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        for k in [self.customer, self.clerk, self.parrot]:
            k.line()


b = Scene()
b.action()

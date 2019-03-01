class Animal:
    #def speak(self):
    #    print('Animal')
    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('Mammal')


class Cat(Mammal):
    def speak(self):
        print('Meow')


class Dog(Mammal):
    def speak(self):
        print('Bark')


class Primate(Mammal):
    def speak(self):
        print('A-A-A')


class Hacker(Primate):
    pass


a = Cat()
a.reply()

b = Hacker()
b.reply()


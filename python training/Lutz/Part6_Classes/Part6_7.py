# The true solution
class Lunch:
    def __init__(self):  # Создать/встроить Customer и Employee
        self.cust = Customer()
        self.empl = Employee()

    def order(self, food_name):  # Начать имитацию оформления заказа
        self.cust.placeOrder(food_name, self.empl)

    def result(self):  # Узнать у клиента название блюда
        self.cust.printFood()


class Customer:
    def __init__(self):  # Инициализировать блюдо значением None
        self.food = None

    def placeOrder(self, food_name, employee):  # Передать заказ официанту
        self.food = employee.takeOrder(food_name)

    def printFood(self):  # Вывести название блюда
        print(self.food.name)


class Employee:
    def takeOrder(self, food_name):  # Вернуть блюдо с требуемым названием
        return Food(food_name)


class Food:
    def __init__(self, name):  # Сохранить название блюда
        self.name = name


if __name__ == '__main__':
    x = Lunch() # Программный код самопроверки выполняется,
    x.order('burritos') # если запускается как сценарий,
    x.result() # а не импортируется как модуль
    x.order('pizza')
    x.result()


## I don't understand this task. My solution:
#class Lunch:
#    def __init__(self, food):
#        self.cust = Customer(food)
#        self.empl = Employee(self.cust)
#
#    def result(self):
#        return self.empl.takeOrder()
#
#
#class Customer:
#    def __init__(self, foodName):
#        self.foodName = foodName
#
#class Employee:
#    def __init__(self, customer):
#        self.cust = customer
#
#    def takeOrder(self):
#        print('order: ', self.cust, self.cust.foodName)
#
#if __name__ == "__main__":
#    a = Lunch('bread')
#    print(a.result())

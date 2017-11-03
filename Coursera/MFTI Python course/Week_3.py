#Coursera homework week3
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        get_photo = self.photo_file_name.split('.')
        photo = get_photo[1]
        return photo

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passengers_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passengers_seats_count = int(passengers_seats_count)

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        list_body_size = self.body_whl.split('x')
        try:
            self.body_size = float(list_body_size[0])*float(list_body_size[1])*float(list_body_size[2])
        except ValueError:
            self.body_size = 0

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for row in reader:
                #print(row)
                car_list.append(row)
    except IOError:
        result = "Error"
        return result

    return car_list


cars = []
trucks = []
spec_macs = []

car_list = get_car_list("week3_cars.csv")
print(car_list)

with open("week3_cars.csv") as csv_file:
    read = csv_file.read()
    #next(read)
    print("file.read:", read)

for i in range(len(car_list)-1):
        if car_list[i][0] == "car":
            car = Car(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][2])
            cars.append(car)
        elif car_list[i][0] == "truck":
            truck = Truck(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][4])
            trucks.append(truck)
        elif car_list[i][0] == "spec_machine":
            spec_mac = SpecMachine(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][6])
            spec_macs.append(spec_mac)
        else:
            print("No such type:", car_list[i][0])

print("cars:", cars)
print("trucks:", trucks)
print("spec_macs:", spec_macs)

for car in range(len(cars)):
    print("photo car:", cars[car].get_photo_file_ext())

for truck in range(len(trucks)):
    print('body_size:', trucks[truck].body_size)
    print("photo:", trucks[truck].get_photo_file_ext())
from models.Car import Car
import csv
class CarOptions:

    def __init__(self):
        self.__car = []

    def add_car(self, car):
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/cars.csv', 'a+') as car_file:
            licence_Plate = car.get_licence_Plate()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            the_Type = car.get_the_Type()
            transmission = car.get_transmission()
            price = car.get_price()
            status = car.get_status()
            car_file.write('{},{},{},{},{},{},{}\n'.format(licence_Plate, category, manufacturer, the_Type, 
                            transmission, price, status))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

    def show_available_cars(self):
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[6] == 'True':
                    print('{:20}{:20}{:20}{:>8} kr.{:>15}'.format(row[2],row[3],row[1],row[5],row[0]))
            print()
            print()
        
    def show_taken_cars(self):
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[6] == 'False':
                    print('{:20}{:20}{:20}{:>8} kr.{:>15}'.format(row[2],row[3],row[1],row[5],row[0]))
            print()
            print()

    def show_Pricelist(self):
        with open("./data/categories.csv") as category_File:
            reader = csv.reader(category_File)
            for row in reader:
                print('{:^25}{:^25}{:^25}'.format(row[0], row[1], row[2]))
            print('-'*75)

        with open("./data/pricelist.csv") as price_File:
            reader = csv.reader(price_File)
            for row in reader:
                print('{:<62}{:<13}'.format(row[0], row[1]))
            print()

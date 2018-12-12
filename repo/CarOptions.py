import csv
import os
from models.Car import Car

class CarOptions:

    def __init__(self):
        self.__car = []

    #Press 1 to Show Available Cars
    def show_available_cars(self):
        ''' Prints out available cars at the moment '''
        available_Cars = []
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[6] == 'True':
                    print('{:20}{:20}{:20}{:>8} kr.{:>15}'.format(row[2],row[3],row[1],row[5],row[0]))
                    available_Cars.append('available')
            if available_Cars == []:
                print('There Are No Available Cars At The Moment\n\n')
            else:
                pass

    # Press 2 to Show Unavailable Cars
    def show_unavailable_cars(self):
        ''' Prints out unavailable cars at the moment '''       
        unavailable_Cars = [] 
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[6] == 'False':
                    print('{:20}{:20}{:20}{:>8} kr.{:>15}'.format(row[2],row[3],row[1],row[5],row[0]))
                    unavailable_Cars.append('unavailable')
            if unavailable_Cars == []:
                print('There Are No Unavailable Cars At The Moment\n\n')
            else:
                pass

    # Press 3 to Show Price List
    def show_Pricelist(self):
        ''' Prints out the price for each category and prices of all individual cars '''
        with open("./data/categories.csv") as category_File:
            reader = csv.reader(category_File)
            for row in reader:
                print('{:^20}{:^20}{:^20}'.format(row[0], row[1], row[2]))
            print('-'*60)

        with open("./data/pricelist.csv") as price_File:
            reader = csv.reader(price_File)
            for row in reader:
                print('{:<47}{:<13}'.format(row[0], row[1]))

    # Press 4 to Add A New Car To The Car Rental       
    def add_car(self, car):
        ''' Adds a new car to The Car Rental (the cars.csv file) '''
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
    


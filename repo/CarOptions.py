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
            print('{:18}{:<20}{:15}{:>8}{:>22}'.format("Manufacturer:","Type:","Category:","Price:","Licence Plate:"))
            for row in reader: 
                if row[6] == 'True':
                    # If the "status" is true then it will print out the information about the car 
                    print('{:18}{:<20}{:15}{:>7} kr.{:>10}'.format(row[2],row[3],row[1],row[5],row[0]))
                    # if it is True, it appends to the list available_cars, so if there are no cars available, 
                    # it will be handled and the user will be noticed about that 
                    available_Cars.append('available')
            if available_Cars == []:
                print('There Are No Available Cars At The Moment')
            else:
                pass

    # Press 2 to Show Unavailable Cars
    def show_unavailable_cars(self):
        ''' Prints out unavailable cars at the moment '''       
        unavailable_Cars = [] 
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            print('{:18}{:<20}{:15}{:>8}{:>22}'.format("Manufacturer:","Type:","Category:","Price:","Licence Plate:"))
            for row in reader:
                if row[6] == 'False':
                    # If the "status" is false then it will print out the information about the car 
                    print('{:18}{:<20}{:15}{:>7} kr.{:>10}'.format(row[2],row[3],row[1],row[5],row[0]))
                    # if it is True, it appends to the list unavailable_cars, so if there are no cars unavailable, 
                    # it will be handled and the user will be noticed about that 
                    unavailable_Cars.append('unavailable')
            if unavailable_Cars == []:
                print('There Are No Unavailable Cars At The Moment')
            else:
                pass

    # Press 3 to Show Price List
    def show_Pricelist(self):
        ''' Prints out the price for each category and prices of all individual cars '''
        with open("./data/categories.csv") as category_File:
            reader = csv.reader(category_File)
            for row in reader:
                # Prints all of the categories the Car rental has 
                print('{:^20}{:^20}{:^20}'.format(row[0], row[1], row[2]))
            print('-'*60)

        with open("./data/cars.csv") as price_File:
            reader = csv.reader(price_File)
            next(price_File) # Skip header row 
            print('{:<20}{:<30}{:^12}'.format("Manufacturer:","Type:","Price:\n"))
            for row in reader:
                # Prints out the manufacturer, type and price of every single car in the car rental
                print('{:<20}{:<30}{:>6} kr.'.format(row[2],row[3],row[5]))

    # Press 4 to Add A New Car To The Car Rental       
    def add_car(self, car):
        '''Adds a new car to The Car Rental (the cars.csv file)'''
        with open('./data/cars.csv', 'a+') as car_file: # a+ = creates file if it doesnt exist
            # this is collecting all of the informations about the car: licence plate, category, manudacturer,
            # type, transmission and price
            # the car status is automatically set to True, because when the car is added it's of course available 
            licence_Plate = car.get_licence_Plate()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            the_Type = car.get_the_Type()
            transmission = car.get_transmission()
            price = car.get_price()
            status = car.get_status()
            # Those informations are then used and written into "cars.csv"
            car_file.write('{},{},{},{},{},{},{}\n'.format(licence_Plate, category, manufacturer, the_Type, 
                    transmission, price, status))
    


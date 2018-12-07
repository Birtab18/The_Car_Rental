from models.Car import Car
import csv
from datetime import date
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
                print('{:^20}{:^20}{:^20}'.format(row[0], row[1], row[2]))
            print('-'*60)

        with open("./data/pricelist.csv") as price_File:
            reader = csv.reader(price_File)
            for row in reader:
                print('{:<47}{:<13}'.format(row[0], row[1]))
            print()

    def put_in_an_order(self,look_up,car_id,a,b,c,e,f,g):
        with open("./data/customers.csv", 'r') as customer_ssn:
         #   look_up = input('Enter The SSN Of The Person who want to rent a car: ')
            reader = csv.reader(customer_ssn)
            for row in reader:
                if row[0] == look_up:
                    customerid = row[0], row[1]
                    print('{}, {}'.format(row[0], row[1]))
        #fa upplysingar um bilinn. 
        with open('./data/cars.csv','r') as order_car:
            # car_id = input('Enter licenche: ')
            lesa = csv.reader(order_car)
            for bar in lesa:
                if bar[0] == car_id:
                    car_id = bar[0],bar[1],bar[2], bar[3]
                    break
                    print('{}, {}, {}, {}'.format(bar[0], bar[1], bar[2], bar[3]))
        # taka inn dagasetningarnar sem vid viljum  panta bilinn. 
        with open('./data/orders.csv', 'a+') as something: 
            SSN = row[0]
            Name = row[1]
            licence_Plate = bar[0]
            category = bar[1]
            manufacturer = bar[2]
            the_Type = bar[3]
            # a = int(input('Y: '))
            # b = int(input('M: '))
            # c = int(input('D: '))
            # e = int(input('Y: '))
            # f = int(input('M: '))
            # g = int(input('D: '))
            returnday = date(a,b,c)
            rentday = date(e,f,g)
            print(returnday)
            print(rentday)
        #   rent_Date
        #   return_Date
            something.write('{},{},{},{},{},{},{}//{} \n'.format(SSN,Name,licence_Plate,category,manufacturer,the_Type, rentday, returnday))

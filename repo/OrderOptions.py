import os
import csv
from models.Order import Order
from datetime import date

class OrderOptions:

    def __init__(self):
        self.__order = []

    # Press 3 to Put In Orders
    def put_in_an_order(self,look_up,car_id,a,b,c,e,f,g):
        with open("./data/customers.csv", 'r') as customer_ssn:
         #   look_up = input('Enter The SSN Of The Person who want to rent a car: ')
            reader_customer = csv.reader(customer_ssn)
            for row in reader_customer:
                if row[0] == look_up:
                    customerid = row[0], row[1]
                    print('{}, {}'.format(row[0], row[1]))
        #fa upplysingar um bilinn. 
        with open('./data/cars.csv','r') as order_car:
            # car_id = input('Enter licenche: ')
            reader_car = csv.reader(order_car)
            for bar in reader_car:
                if bar[0] == car_id:
                    car_id = bar[0],bar[1],bar[2], bar[3]
                    break
                    print('{}, {}, {}, {}'.format(bar[0], bar[1], bar[2], bar[3]))
        # taka inn dagasetningarnar sem vid viljum  panta bilinn. 
        with open('./data/orders.csv', 'a+') as order_file: 
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
            order_file.write('{},{},{},{},{},{},{},{} \n'.format(SSN,Name,licence_Plate,category,manufacturer,the_Type, rentday, returnday))



    # Press 4 to Cancel Order
    def delete_customer(self):
        with open('./data/customers.csv', 'a+') as customer_file:
            customer_Delete = input("Enter Customers SSN number: ")
            for line in customer_file.readlines():
                if line not in customer_Delete:
                    customer_file.write(line)
        return self.__customer 

    # Press 5 to Look Up Order
    def look_Up_Order(self, look_Up):
        with open("./data/orders.csv", 'r') as look_up_order_file:
            reader = csv.reader(look_up_order_file)
            for row in reader:
                match = []
                if row[2] == look_Up:
                    match.append('found')
                    print('Customer Informations\n{}'.format("-"*20))
                    print('SSN:{:<10}\nName:{:>30}\n'.format(row[0],row[1]))
                    print('Car Informations:\n{}'.format("-"*35))
                    print('Licence Plate: {:>13}\nCategory: {:>21}\nManufacturer: {:>12}\nType: {:>24}\n'.
                            format(row[2], row[3], row[4],row[5]))
                    print('Order Informations:\n{}'.format("-"*35))
                    print('Rent Date: {:>22}\nReturn Date: {:>20}\nExtra Insurance: {:>10}'.format(row[6], row[7], row[8]))
            # if match == []:
            #     print('Order Not Found')
            #     print()
          
    
    # Press 6 to Change Order
    def change_Order(self):
        pass

    

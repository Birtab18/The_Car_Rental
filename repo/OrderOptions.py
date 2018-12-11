import os
import csv
from models.Order import Order
from datetime import date

class OrderOptions:

    def __init__(self):
        self.__order = []

    def car_check(self, car_id):
        with open("./data/cars.csv", 'r') as car_check:
            reader = csv.reader(car_check)
            for row in reader:
                main_checking = True
                while main_checking :
                    if row[6] == 'False':
                        print('This car is unavailable at this moment!')
                        print('Try again!')
                        break
                    else:
                        print('Found!')
                        main_checking = False

    # Press 1 to Put In Orders
    def put_in_an_order(self,SSN,car_id,car_rent_year,car_rent_month,car_rent_day,car_return_year,
            car_return_month,car_return_day,total_price):
        ''' Adds an order to The Car Rental (the orders.csv file) '''
        with open("./data/customers.csv", 'r') as customer_File:
            reader_customer = csv.reader(customer_File)
            for row in reader_customer:
                if row[0] == SSN:
                    break
                    print('{}, {}'.format(row[0], row[1]))
        #fa upplysingar um bilinn. s
        with open('./data/cars.csv','r') as order_car:
            reader_car = csv.reader(order_car)
            for bar in reader_car:
                if bar[0] == car_id:
                    break
                    print('{}, {}, {}, {}'.format(bar[0], bar[1], bar[2], bar[3]))
        
        # taka inn dagasetningarnar sem vid viljum panta bilinn. 
        with open('./data/orders.csv', 'a+') as order_file: 
            SSN= row[0]
            Name = row[1]
            licence_Plate = bar[0]
            category = bar[1]
            manufacturer = bar[2]
            the_Type = bar[3]
            returnday = date(car_rent_year,car_rent_month,car_rent_day)
            rentday = date(car_return_year,car_return_month,car_return_day)
            differece =  rentday.day - returnday.day
            multiply = differece * int(bar[5])
            #extra insurence
            if total_price =='y':
                total_price_main = int(multiply*1.25)
            elif total_price == 'n':
                total_price_main = int(multiply)
            else:
                print('Invalid input')
            order_file.write('{},{},{},{},{},{},{},{},{}kr.-\n'.format(SSN,Name,licence_Plate,category,
                    manufacturer,the_Type,rentday,returnday,total_price_main))
        #fall sem breytir yfir i false. 
        with open('./data/cars.csv', 'r') as inp, open('./data/deletecars.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['licence_Plate','category','manufacturer','the_Type',
                    'transmission','price','status'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i,value in row.items():
                    if value == car_id:
                        if row['status'] == 'True':
                            row['status'] = 'False'
                writer.writerow(row)
        os.remove('./data/cars.csv')
        os.rename('./data/deletecars.csv', './data/cars.csv')




    # Press 2 to Cancel Order
    def cancel_Order(self, SSN, licence_Plate):
        ''' Cancels an order from The Car Rental (from the orders.csv file) '''
        with open('./data/orders.csv', 'r') as inp, open('./data/cancel_Order.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer', 
                    'the_Type', 'rent_Date', 'return_Date', 'total_price_main'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN'] != SSN and row['licence_Plate'] != licence_Plate:
                    writer.writerow(row)
        os.remove('./data/orders.csv')
        os.rename('./data/cancel_Order.csv', './data/orders.csv')

    # Press 3 to Look Up Order
    def look_Up_Order(self, SSN, licence_Plate):
        ''' Looks up an order in The Car Rental (in the orders.csv file) '''
        with open("./data/orders.csv", 'r') as look_up_order_file:
            reader = csv.reader(look_up_order_file)
            for row in reader:
                match = []
                if row[0] == SSN and row[2] == licence_Plate:
                    match.append('found')
                    print('Customer Informations\n{}'.format("-"*35))
                    print('SSN:{:>20}{}\nName:{:>19}{}\n'.format(" ",row[0]," ",row[1]))
                    print('Car Informations:\n{}'.format("-"*35))
                    print('Licence Plate:{:>10}{}\nCategory:{:>15}{}\nManufacturer:{:>11}{}\nType:{:>19}{}\n'.
                            format(" ",row[2]," ",row[3]," ", row[4]," ",row[5]))
                    print('Order Informations:\n{}'.format("-"*35))
                    print('Rent Date:{:>14}{}\nReturn Date:{:>12}{}\nTotal price:{:>8}{}'.format(" ",row[6],
                            " ", row[7]," ", row[8]))
            # if match == []:
            #     print('Order Not Found')
            #     print()
          
    
    # Press 4 to Change Order
    def change_Order(self, SSN, choice, changes):
        ''' Changes an order in The Car Rental (in the orders.csv file). Changes category, the date of the rent,
        the date of the return or/and if the customer want an extra insurance '''
        with open('./data/orders.csv', 'r') as inp, open('./data/delete_Orders.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer', 
                    'the_Type', 'rent_Date', 'return_Date', 'total_price_main'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i,value in row.items():
                    if value == SSN: #i lagi að gera rað f að aðili se bara með 1 pöntun?
                        the_Choice = ''
                        if choice == '1':
                            the_Choice ='category'
                            # if len(the_Choice) == 10:
                            #     row[the_Choice] = changes
                        elif choice == '2':
                            the_Choice = 'rent_Date'
                        elif choice == '3':
                            the_Choice = 'return_Date'
                        elif choice == '4':
                            the_Choice = 'total_price_main'
                        row[the_Choice] = changes
                writer.writerow(row)
        os.remove('./data/orders.csv')
        os.rename('./data/delete_Orders.csv', './data/orders.csv')

    def print_orders(self):
        with open("./data/orders.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                print('{:20}{:20}{:20}{:20}{:20}{:20}{:20}{:20}{:20}'.format(row[0],row[1],row[2],row[3],row[4],
                        row[5],row[6],row[7],row[8]))
            
    def return_car(self, plate):
        with open('./data/cars.csv', 'r') as inp, open('./data/deletecars.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['licence_Plate','category','manufacturer','the_Type','transmission','price','status'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i,value in row.items():
                    if value == plate:
                        if row['status'] == 'False':
                            row['status'] = 'True'
                        print(row)
                writer.writerow(row)
        os.remove('./data/cars.csv')
        os.rename('./data/deletecars.csv', './data/cars.csv')

        with open('./data/orders.csv', 'r') as inp, open('./data/cancel_Order.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer', 
                    'the_Type', 'rent_Date', 'return_Date', 'total_price_main'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['licence_Plate'] != plate:
                    writer.writerow(row)
        os.remove('./data/orders.csv')
        os.rename('./data/cancel_Order.csv', './data/orders.csv')



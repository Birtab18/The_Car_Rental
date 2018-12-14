import csv
import os
from models.Order import Order
from datetime import date

class OrderOptions:

    def __init__(self):
        self.__order = []

    def pick_a_category(self, car_choice):
        ''' Prints out available cars at the moment, and allows the user to choose category '''
        available_Cars = []
        with open("./data/cars.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[6] == 'True' and row[1] == car_choice:
                    print('{:15}{:15}{:15}{:>8} kr.{:>15}'.format(row[2], row[3], row[1], row[5], row[0]))
                    available_Cars.append('available')
            if available_Cars == []:
                print('There Are No Available Cars At The Moment\n\n')
            else:
                pass

    def check_Car(self, licence_Plate):
        ''' To check if the car exists and is available, if so it returns True'''
        with open("./data/cars.csv", 'r') as check_Car:
            reader = csv.reader(check_Car)
            for row in reader:
                if row[6] == 'True' and row[0] == licence_Plate:
                    return True

    
    def check_Order(self, SSN):
        ''' Check if the order exists or not, if so it returns True '''
        with open("./data/orders.csv", 'r') as check_Order:
            reader = csv.reader(check_Order)
            for row in reader:
                if row[0] == SSN:
                    return True

    # Press 1 to Put In Orders
    def put_in_an_order(self, SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day, car_return_year,
            car_return_month, car_return_day, extra_insurance):
        ''' Adds an order for today to The Car Rental (the orders.csv file) '''
        # Get informations about the Customer that is putting in the order 
        with open("./data/customers.csv", 'r') as customer_File:
            reader_customer = csv.reader(customer_File)
            for row in reader_customer:
                # If there is a match it will go out of the loop
                if row[0] == SSN:
                    break

        # Get informations about the car the costumer is renting
        with open('./data/cars.csv', 'r') as order_car:
            reader_car = csv.reader(order_car)
            for bar in reader_car:
                # If there is a match it will go out of the loop
                if bar[0] == licence_Plate:
                    break

        # Collect all of the informations from customers and cars that we need
        with open('./data/orders.csv', 'a+') as order_file:
            SSN = row[0]
            Name = row[1]
            licence_Plate = bar[0]
            category = bar[1]
            manufacturer = bar[2]
            the_Type = bar[3]
            # Get the rent day and return day 
            rentday = date(car_rent_year, car_rent_month, car_rent_day)
            returnday = date(car_return_year, car_return_month, car_return_day)
            days = returnday.day - rentday.day #How many days is the renting
            rent_Price = days * int(bar[5]) #days * price per. day
            VAT = 1.20
            # extra insurence
            if extra_insurance == 'y':
                total_price = int((rent_Price * 1.25) * VAT)
                print("\nTotal Price:  {}kr.".format(total_price)) 
            elif extra_insurance == 'n':
                total_price = int(rent_Price * VAT)
                print("\nTotal Price:  {}kr.".format(total_price)) 
            else:
                print('Invalid input')

            # Put in the order into "orders.csv"  
            order_file.write('{},{},{},{},{},{},{},{},{}kr.-\n'.format(SSN, Name, licence_Plate, category,
                    manufacturer, the_Type, rentday, returnday, total_price))

        # Make car unavailable (True to False)
        with open('./data/cars.csv', 'r') as inp, open('./data/deletecars.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['licence_Plate', 'category', 'manufacturer', 'the_Type',
                    'transmission', 'price', 'status'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i, value in row.items():
                    if value == licence_Plate:
                        if row['status'] == 'True':
                            row['status'] = 'False'
                writer.writerow(row)
        #This deletes the old file, with the old informations
        os.remove('./data/cars.csv')
        # This renames "deletecars" to "cars", like the old one with all of the old
        # information exept for the one that was changed
        os.rename('./data/deletecars.csv', './data/cars.csv')

    def put_in_future_order(self, SSN, Name, Category, car_rent_year, car_rent_month, car_rent_day, car_return_year,
            car_return_month, car_return_day, extra_insurance):
        ''' Keeps information about future orders, fx. orders for tomorrow or anywhere in the future.'''
        with open('./data/futureorders.csv', 'a+') as order_file: # a+ creates the file if it doesn't exist
            # This dosen't do anything in the system except keeping track of the orders
            # Then the user needs to automaticly transfer the orders in to "put in order" 
            SSN = SSN
            Name = Name
            Category = Category
            Rentday = date(car_rent_year, car_rent_month, car_rent_day)
            Returnday = date(car_return_year, car_return_month, car_return_day)
            ExtraInsurance = extra_insurance
            # Put the informations about the customer, the category that he prefers, rent date and return day 
            # into "futureorders.csv"
            order_file.write('{},{},{},{},{},{}\n'.format(SSN, Name, Category, Rentday, Returnday, ExtraInsurance))

    def print_out_future_orders(self):
        '''This prints out everything that is in future orders, a reminder for the user so he can put in orders 
        if there are any for today'''
        # Prints out whenever the user is going to put in the order
        with open('./data/futureorders.csv', 'r') as order_car:
            reader_car = csv.reader(order_car)
            for bar in reader_car:
                print('{:10} {:15} {:15} {:15} {:15} {:15}'.format(bar[0], bar[1], bar[2], bar[3], bar[4], bar[5]))

    def remove_from_future_orders(self, SSN_input):
        '''Removes orders from future orders when the order has been done'''
        with open('./data/futureorders.csv', 'r') as inp, open('./data/deletefutureorders.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'Category', 'Rentday', 'Returnday', 
                    'ExtraInsurance'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN'] != SSN_input:
                    writer.writerow(row)
        #This deletes the old file, with the old informations
        os.remove('./data/futureorders.csv')
        # This renames "deletefutureorders" to "future orders", 
        # like the old one with all of the orders except the ones that were transfered over
        os.rename('./data/deletefutureorders.csv', './data/futureorders.csv')

    # Press 2 to Cancel Order
    def cancel_Order(self, SSN):
        ''' Cancels an order from The Car Rental (from the orders.csv file) '''
        with open('./data/orders.csv', 'r') as inp, open('./data/cancel_Order.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer',
                    'the_Type', 'rent_Date', 'return_Date', 'total_price'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN'] != SSN:
                    writer.writerow(row)
        os.remove('./data/orders.csv')
        os.rename('./data/cancel_Order.csv', './data/orders.csv')

    # Press 3 to Look Up Order
    def look_Up_Order(self, SSN):
        print()
        ''' Looks up an order in The Car Rental (in the orders.csv file) '''
        with open("./data/orders.csv", 'r') as look_up_order_file:
            reader = csv.reader(look_up_order_file)
            # It iterates through every row in the file, to try to find a match
            for row in reader:
                if row[0] == SSN:
                    # If the SSN input matches index [0] it will print all the informations about the costumer
                    print('Customer Informations\n{}'.format("-"*35))
                    print('SSN:{:>20}{}\nName:{:>19}{}\n'.format( " ", row[0], " ", row[1]))
                    print('Car Informations:\n{}'.format("-"*35))
                    print('Licence Plate:{:>10}{}\nCategory:{:>15}{}\nManufacturer:{:>11}{}\nType:{:>19}{}\n'.
                          format(" ", row[2], " ", row[3], " ", row[4], " ", row[5]))
                    print('Order Informations:\n{}'.format("-"*35))
                    print('Rent Date:{:>14}{}\nReturn Date:{:>12}{}\nTotal price:{:>12}{}'.format(" ", row[6],
                          " ", row[7], " ", row[8]))

    # Press 4 to Change Order
    def change_Order(self, SSN, choice, changes):
        ''' Changes an order in The Car Rental (in the orders.csv file). Changes category, the date of the rent,
        the date of the return or/and if the customer want an extra insurance '''
        with open('./data/orders.csv', 'r') as inp, open('./data/delete_Orders.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer',
                    'the_Type', 'rent_Date', 'return_Date', 'total_price'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i, value in row.items():
                    if value == SSN:
                        the_Choice = ''
                        if choice == '1':
                            the_Choice = 'rent_Date'
                        elif choice == '2':
                            the_Choice = 'return_Date'
                        elif choice == '3':
                            the_Choice = 'total_price'
                        row[the_Choice] = changes
                writer.writerow(row)
        os.remove('./data/orders.csv')
        os.rename('./data/delete_Orders.csv', './data/orders.csv')

    def print_orders(self):
        ''' Prints out all of the orders that are active '''
        # This is used whenever someone is returning a car, then we can se his/hers order
        with open("./data/orders.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            next(look_up_customer_file)
            print('{:<15}{:<25}{:<20}{:<20}{:<20}{:<20}{:<20}'.format("SSN:","Name:","Licence Plate:",
                    "Manufacturer:","The Type:","Rent Day:","Return Day:"))
            for row in reader:
                print('{:<15}{:<25}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(row[0], row[1], row[2], row[4], row[5],
                        row[6], row[7]))

    def return_car(self, plate):
        ''' When the car is returned the user needs to return it manually '''
        with open('./data/cars.csv', 'r') as inp, open('./data/deletecars.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['licence_Plate', 'category', 'manufacturer', 'the_Type',
                    'transmission', 'price', 'status'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i, value in row.items():
                    if value == plate:
                        #Change the status on the car to True, so now it's available again
                        if row['status'] == 'False':
                            row['status'] = 'True'
                writer.writerow(row)
        os.remove('./data/cars.csv')
        os.rename('./data/deletecars.csv', './data/cars.csv')
        # creates a new file called cars, like the old one, with all it's content but the car we just returned
        # is now marked true (available)

        with open('./data/orders.csv', 'r') as inp, open('./data/cancel_Order.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN', 'Name', 'licence_Plate', 'category', 'manufacturer',
                    'the_Type', 'rent_Date', 'return_Date', 'total_price'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['licence_Plate'] != plate:
                    writer.writerow(row)
        os.remove('./data/orders.csv') 
        os.rename('./data/cancel_Order.csv', './data/orders.csv')
        # creates a new file called orders, like the old one, with all it's content but the car we just returned
        # is not there

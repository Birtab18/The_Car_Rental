import csv
import os
from services.OrderService import OrderService
<<<<<<< HEAD
from services.CustomerService import CustomerService
=======
from services.CarService import CarService
>>>>>>> 31fc2173783815727d68e027716327b8277a5b8e
from models.Order import Order


class Order_Page:
    def __init__(self):
        self.__OrderService = OrderService()
        self.__CarService = CarService()

    def Order_Menu(self):

        def print_Choices():
            ''' Prints out everything you can do with orders in the system '''
            print('{:<30}{:>20}'.format('The Car Rental', 'F To Go to Frontpage'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Put In Order')
            print('Press 2 to Cancel Order') 
            print('Press 3 to Look Up Order')
            print('Press 4 to Change Order')
            print('Press F to Go To Frontpage')
            print()

        def main():
            print_Choices()
            print()
            action = ""
            while action not in ["1","2","3","4","F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*15)
<<<<<<< HEAD
                    new_Or_Old = input('Has the customer rented a car from us before? (y = Yes, n = No) ').lower()
                    while new_Or_Old != 'y' or 'n':
                        if new_Or_Old == 'y':
                            # go to look up customer
                            # SSN = ('Enter The SSN Of The Person You Want To Look Up: ')
                            # lookup = CustomerService()
                            # lookup.look_up_customer(SSN)
                            pass
                        elif new_Or_Old == 'n':
                            # go to sign up new customer
                            # signup = CustomerService()
                            # signup.add_customer()
                            pass
                        else:
                            print('Invalid input, try again!')
                    self.__OrderService.print_available_cars()
=======
                    # new_Or_Old = input(
                    #     'Has the customer rented a car from us before? y = Yes, n = No').lower()
                    # while new_Or_Old != 'y' or 'n':
                    #     if new_Or_Old == 'y':
                    #         # go to look up customer
                    #         pass
                    #     elif new_Or_Old == 'n':
                    #         # go to sign up new customer
                    #         pass
                    #     else:
                    #         print('Invalid input, try again!')
                    self.__CarService.available_cars()
>>>>>>> 31fc2173783815727d68e027716327b8277a5b8e
                # print("New Order:")
                # licence_Plate = input('Enter The Licence Plate: ')
                # # þurfum að leita upp línunni í cars með þetta nr og taka þær uppl og setja i orders
                # # með uppl um vv
                # # notum daytime moduleinn her?
                # rent_Date = input('Enter The Date Of The Rent: ')
                # # like her daytime?
                # return_Date = input('Enter The Date Of The Return: ')
                # insurance = input('Extra insurance? (Y = Yes, N = No) ')
                # new_Order = Order(the_Customer, the_Car, rent_Date, return_Date, insurance)
                    # print('Availeble cars: ')
                    # with open("./data/cars.csv", 'r') as look_up_customer_file:
                    #     reader = csv.reader(look_up_customer_file)
                    #     for row in reader:
                    #         if row[6] == 'True':
                    #             print('{:20}{:20}{:20}{:>8} kr.{:>15}'.format(row[2],row[3],row[1],row[5],row[0]))
                    look_up = input('Enter The SSN Of The Person who want to rent a car: ')
                    while len(look_up) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)')
                        print()
                        look_up = input('Enter The SSN Of The Person who want to rent a car: ')
                    car_id = input('Enter The Licence Plate Of The Car: ')
                    print("Enter Rent Date")
                    print("-"*15)
                    car_rent_year = int(input('Enter Rent Year: '))
                    car_rent_month = int(input('Enter Rent Month: '))
                    car_rent_day = int(input('Enter Rent Day: '))
                    print("Enter Return Date")
                    car_return_year = int(input('Enter Return Year: '))
                    car_return_month = int(input('Enter Return Month: '))
                    car_return_day = int(input('Enter Return Day: '))
                    extra_insurence = input('Do you want extra insurence: Press(Y) for Yes and Press(N) for No ').lower()
                    self.__OrderService.put_in_an_order(look_up,car_id,car_rent_year,car_rent_month,car_rent_day,car_return_year,car_return_month,car_return_day,extra_insurence)

                elif action == '2':
                    print("-"*15)
                    SSN = input('Enter The SSN Of The Person Who Put In The Order: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)')
                        print()
                        SSN = input('Enter The SSN of The Person Who Put In The Order: ')
                    licence_Plate = input('Enter The Licence Plate Of The Car: ')
                    self.__OrderService.cancel_Order(SSN, licence_Plate)

                elif action == '3':
                    print("-"*15)
                    SSN = input('Enter The SSN of The Person Who Put In The Order: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)')
                        print()
                        SSN = input('Enter The SSN of The Person Who Put In The Order: ')
                    licence_Plate = input('Enter The Licence Plate Of The Car: ')
                    print()
                    self.__OrderService.look_up_order(SSN,licence_Plate)
                    print()

                elif action == '4':
                    print("-"*15)
                    print()
                    print('press 1 to Change Category (Mini Car, Station Car Or Jeep)')
                    print('Press 2 to Change Rent Date')
                    print('Press 3 to Change Return Date')
                    print('Press 4 to Change Extra Insurance (Y = Yes, N = No')
                    print()
                    SSN = input('Enter The SSN Of The Person Who Ordered The Car: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)')
                        print()
                        SSN = input('Enter The SSN Of The Person Who Ordered The Car: ')
                    choice = input('Enter Choice: ')
                    changes = input('Enter New Info: ').lower()
                    self.__OrderService.change_Order(SSN, choice, changes)
                
                elif action == 'f':
                    break
                else:
                    print("Invalid input, try again!")

        main()

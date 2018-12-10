import csv
import os
from services.OrderService import OrderService
from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Order import Order
from models.Customer import Customer
from repo.CustomerOptions import CustomerOptions

class Order_Page:
    def __init__(self):
        self.__OrderService = OrderService()
        self.__CarService = CarService()
        self.__Customer = CustomerOptions()
        self.__CustomerService = CustomerService()

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
                    new_Or_Old = input('Has the customer rented a car from us before? (y = Yes, n = No) ').lower()
                    while new_Or_Old != 'y' or 'n':
                        if new_Or_Old == 'y':
                            break
                        elif new_Or_Old == 'n':
                            print("Signing A New Customer:")
                            print("-"*15)
                            SSN = input('Enter A SSN: ')
                            while len(SSN) != 10:
                                print('Error! Please Input A Valid SSN (only 10 digits)')
                                print()
                                SSN = input('Enter A SSN: ')
                            name = input('Enter a name: ')
                            phonenumber = input('Enter a phonenumber: ')
                            email = input('Enter an email: ')
                            new_Costumer = Customer(SSN, name, phonenumber, email)
                            self.__CustomerService.add_customer(new_Costumer)
                            break
                        else:
                            print('Invalid input, try again!')
                        
                    self.__CarService.available_cars()
                    SSN = input('Enter The SSN Of The Person who want to rent a car: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)')
                        print()
                        SSN = input('Enter The SSN Of The Person who want to rent a car: ')
                    car_id = input('Enter The Licence Plate Of The Car: ')
                    print("-"*15)
                    car_rent_year = int(input('Enter Rent Year: '))
                    car_rent_month = int(input('Enter Rent Month: '))
                    car_rent_day = int(input('Enter Rent Day: '))
                    print("-"*15)
                    car_return_year = int(input('Enter Return Year: '))
                    car_return_month = int(input('Enter Return Month: '))
                    car_return_day = int(input('Enter Return Day: '))
                    extra_insurence = input('Do you want extra insurence: Press(Y) for Yes and Press(N) for No ').lower()
                    self.__OrderService.put_in_an_order(SSN,car_id,car_rent_year,car_rent_month,car_rent_day,
                            car_return_year,car_return_month,car_return_day,extra_insurence)

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
                    print('\nOrder Changed!\n\n')
                
                elif action == 'f':
                    break

                else:
                    print("Invalid input, try again!")

        main()

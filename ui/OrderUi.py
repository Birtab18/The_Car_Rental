import csv
import os
from services.OrderService import OrderService
from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Order import Order
from models.Customer import Customer
from repo.CustomerOptions import CustomerOptions


class Order_UI:
    def __init__(self):
        self.__OrderService = OrderService()
        self.__CarService = CarService()
        self.__Customer = CustomerOptions()
        self.__CustomerService = CustomerService()

    def Order_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with orders in the system '''
            print('{:<30}{:>30}'.format('The Car Rental', 'F To Go to Frontpage'))
            print('-'*60)
            print("{:^60}".format('ORDERS'))
            print('-'*60)
            print('Press 1 to Put In Order')
            print('Press 2 to Cancel Order')
            print('Press 3 to Look Up Order')
            print('Press 4 to Change Order')
            print('Press 5 to Return Car')
            print('Press F to Go To Frontpage\n')

        def main():
            print_Choices()
            action = ""
            while action not in ["1", "2", "3", "4", "F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*60)
                    new_Or_Old = input('Has the customer rented a car from us before? (y = Yes, n = No) ').lower()
                    while new_Or_Old != 'y' or 'n':
                        if new_Or_Old == 'y':
                            print()
                            break
                        elif new_Or_Old == 'n':
                            print("Signing A New Customer:")
                            print("-"*60)
                            SSN_input = input('Enter The SSN Of The Person Who Is Putting In An Order: ')
                            SSN = self.__CustomerService.check_SSN(SSN_input)
                            name = input('Enter a name: ')
                            phonenumber_input = input('Enter a Phone Number: ')
                            phonenumber = self.__CustomerService.check_Phonenumber(phonenumber_input)
                            email = input('Enter an email: ')
                            new_Costumer = Customer(
                                SSN, name, phonenumber, email)
                            self.__CustomerService.add_customer(new_Costumer)
                            print()
                            break
                        else:
                            print('Invalid input, try again!')
                    print('Available cars: ')
                    self.__CarService.available_cars()
                    SSN_input = input('Enter The SSN Of The Person Who Is Putting In An Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    licence_Plate = input('Enter The Licence Plate Of The Car: ')
                    isFound = self.__OrderService.check_Car(licence_Plate)
                    while not isFound:
                        print("Car not found \nPlease try again!")
                        licence_Plate = input('Enter The Licence Plate Of The Car: ').upper()
                        isFound = self.__OrderService.check_Car(licence_Plate)
                    print("-"*60)
                    car_rent_year = int(input('Enter Rent Year: '))
                    car_rent_month = int(input('Enter Rent Month: '))
                    car_rent_day = int(input('Enter Rent Day: '))
                    print("-"*60)
                    car_return_year = int(input('Enter Return Year: '))
                    car_return_month = int(input('Enter Return Month: '))
                    car_return_day = int(input('Enter Return Day: '))
                    extra_insurence = input('Do you want extra insurence: Press(Y) for Yes and Press(N) for No ').lower()
                    payment = input('Are you paying with a Card or Cash: (Press 1 for Card , Press 2 for Cash) ')
                    if payment == '1':
                        cardholder = input("Enter The Cardholder's Name: ")
                        card = ''
                        card = input('Enter Your Card Number: ')
                        while len(card) != 16:
                            print( 'Error! Please Input A Valid Card Number (only 16 digits)\n')
                            card = input('Enter Your Card Number: ')
                        exp_date = input('Enter Cards Expiry Date: ')
                        sec_num = input('Enter The Security Number:')
                        print('Payment Completed!')
                    if payment == '2':
                        print('Payment Completed!')
                    self.__OrderService.put_in_an_order(SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day,
                                                        car_return_year, car_return_month, car_return_day, extra_insurence)
                    print('\nOrder Added!\n\n')

                elif action == '2':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    print()
                    isFound = self.__OrderService.check_Order(SSN)
                    while not isFound:
                        print("\nOrder not found! Please try again!\n")
                        SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                        SSN = self.__CustomerService.check_SSN(SSN_input)
                        print()
                        isFound = self.__OrderService.check_Order(SSN)
                    self.__OrderService.cancel_Order(SSN)
                    print('\nOrder Canceled!\n\n')

                elif action == '3':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    print()
                    isFound = self.__OrderService.check_Order(SSN)
                    while not isFound:
                        print("\nOrder not found! Please try again!\n")
                        SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                        SSN = self.__CustomerService.check_SSN(SSN_input)
                        print()
                        isFound = self.__OrderService.check_Order(SSN)
                    self.__OrderService.look_up_order(SSN)
                    print()

                elif action == '4':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    while not isFound:
                        print("Order not found! Please try again!\n")
                        SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                        SSN = self.__CustomerService.check_SSN(SSN_input)
                        isFound = self.__CustomerService.check_Costumer(SSN)
                    self.__OrderService.look_up_order(SSN)
                    print('\n\nPress 1 to Change Rent Date')
                    print('Press 2 to Change Return Date')
                    print('Press 3 to Change Extra Insurance (Y = Yes, N = No)\n')
                    choice_input = input('Enter Choice: ')
                    choice = self.__CustomerService.check_Choice(choice_input)
                    changes = input('Enter New Info: ').lower()
                    self.__OrderService.change_Order(SSN, choice, changes)
                    print('\nOrder Changed!\n\n')

                elif action == '5':
                    print("-"*60)
                    print('Return car: \n')
                    self.__OrderService.print_orders()
                    plate = input('\nEnter The Licence Plate Of The Car You Want To Return: ')
                    self.__OrderService.return_car(plate)
                    print('\nCar Returned!\n\n')

                elif action == 'f':
                    break

                else:
                    print("Invalid input, try again!")

        main()

import csv
import os
from services.OrderService import OrderService
from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Order import Order
from models.Customer import Customer
from repo.CustomerOptions import CustomerOptions
from datetime import datetime
            
class Put_In_Order_UI:
    def __init__(self):
        self.__OrderService = OrderService()
        self.__CarService = CarService()
        self.__Customer = CustomerOptions()
        self.__CustomerService = CustomerService()


    def Put_In_Order_Menu(self):
        def print_Choices():
            print('\nPress 1 to Put In Order')
            print('Press 2 to Put in a Future Order\n')
        
        def main():
            print_Choices()
            action = ""
            while action not in ["1", "2"]:
                action = input('Choose command: ').lower()

            # Press 1 to Put In Order

            if action == '1':
                #Prenta út thad sem stendur i futureorders.csv skranni. og segja 
                print('Are there any Orders You have to activate today?')
                self.__OrderService.print_out_future_orders()
                
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
                loop = True
                while loop:
                    car_choice = input('What kind of car do you want?\nPress (M) for Mini car\nPress (S) for Station car\nPress (J) for Jeep\nChoose a category:').lower()
                    if car_choice == 'm':
                        print("-"*60)
                        car_choice = 'Mini Car'
                        print('These Mini Cars are available:')
                        self.__OrderService.pick_a_category(car_choice)
                        loop = False
                        break
                    elif car_choice == 's':
                        print("-"*60)
                        car_choice = 'Station Car'
                        print('These Station Cars are available:')
                        self.__OrderService.pick_a_category(car_choice)
                        loop = False
                        break
                    elif car_choice == 'j':
                        print("-"*60)
                        car_choice = 'Jeep'
                        print('These Jeeps are available:')
                        self.__OrderService.pick_a_category(car_choice)
                        loop = False
                        break
                    else:
                        print('Wrong input')
                print("-"*60)
                SSN_input = input('Enter The SSN Of The Person Who Is Putting In An Order: ')
                self.__OrderService.remove_from_future_orders(SSN_input)
                SSN = self.__CustomerService.check_SSN(SSN_input)
                print("-"*60)
                licence_Plate = input(
                    'Enter The Licence Plate Of The Car: ').upper()
                isFound = self.__OrderService.check_Car(licence_Plate)
                while not isFound:
                    print("Car not found \nPlease try again!")
                    licence_Plate = input(
                        'Enter The Licence Plate Of The Car: ').upper()
                    isFound = self.__OrderService.check_Car(licence_Plate)
                print("-"*60)
                car_rent_year = int(input('Enter Rent Year: '))
                car_rent_month = int(input('Enter Rent Month: '))
                car_rent_day = int(input('Enter Rent Day: '))
                print("-"*60)
                car_return_year = int(input('Enter Return Year: '))
                car_return_month = int(input('Enter Return Month: '))
                car_return_day = int(input('Enter Return Day: '))
                print("-"*60)
                extra_insurance = input(
                    'Do you want extra insurance: Press(Y) for Yes and Press(N) for No: ').lower()
                print("-"*60)
                if extra_insurance == 'y':
                    print('We need your Credit Card Number please\n')
                    credit_card = input('Enter your Credit Card Number:')
                    while len(credit_card) != 16:
                        print(
                            'Error! Please Input A Valid Credit Card Number (only 16 digits)\n')
                        credit_card = input(
                            'Enter your Credit Card Number:')
                print("-"*60)
                payment = input(
                    'Are you paying with a Card or Cash: (Press 1 for Card , Press 2 for Cash): ')
                print("-"*60)
                if payment == '1':
                    cardholder = input("Enter The Cardholder's Name: ")
                    card = ''
                    card = input('Enter Your Card Number: ')
                    while len(card) != 16:
                        print(
                            'Error! Please Input A Valid Card Number (only 16 digits)\n')
                        card = input('Enter Your Card Number: ')
                    exp_date = input('Enter Cards Expiry Date: ')
                    sec_num = input('Enter The Security Number:')
                    print('Payment Completed!')
                if payment == '2':
                    print('Payment Completed!')
                self.__OrderService.put_in_an_order(SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day,
                                                    car_return_year, car_return_month, car_return_day, extra_insurance)
                print('\nOrder Added!')

            elif action == '2':
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
                        self.__OrderService.remove_from_future_orders(SSN_input)
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
                SSN = input('Enter SSN: ')
                Name = input('Enter Name: ')
                licence_Plate = input('Enter licence plate: ')
                car_rent_year = int(input('Enter Rent Year: '))
                car_rent_month = int(input('Enter Rent Month: '))
                car_rent_day = int(input('Enter Rent Day: '))
                print("-"*60)
                car_return_year = int(input('Enter Return Year: '))
                car_return_month = int(input('Enter Return Month: '))
                car_return_day = int(input('Enter Return Day: '))
                extra_insurance = input('Do you want extra insurance? ')
                self.__OrderService.put_in_future_order(SSN,Name,licence_Plate,car_rent_year,car_rent_month,car_rent_day,car_return_year,car_return_month,
                car_return_day,extra_insurance)


        main()
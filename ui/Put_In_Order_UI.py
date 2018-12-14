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
            print('\nPress 1 To Put In Order')
            print('Press 2 To Put In A Future Order\n')

        def new_Or_Old():
            print("-"*80)
            new_Or_Old = input('Has The Customer Rented From Us Before? (Y = Yes, N = No) ').lower()
            while new_Or_Old != 'y' or 'n':
                if new_Or_Old == 'y':
                    print()
                    break
                elif new_Or_Old == 'n':
                    print("\nSigning A New Customer:")
                    print("-"*80)
                    SSN_input = input('Enter The SSN Of The Person Who Is Putting In An Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isfound = self.__CustomerService.check_Costumer(SSN)
                    if isfound:
                        print('\nCustomer Already Exists!')
                    else:
                        name = input('Enter A Name: ')
                        phonenumber_input = input('Enter A Phone Number: ')
                        phonenumber = self.__CustomerService.check_Phonenumber(phonenumber_input)
                        email = input('Enter An Email: ')
                        new_Costumer = Customer(SSN, name, phonenumber, email)
                        self.__CustomerService.add_customer(new_Costumer)
                        print("\nCostumer Signed!\n\n")
                        break
                else:
                    print('Invalid Input, Try Again!')
                    new_Or_Old = input('Has The Customer Rented A Car From Us Before? (Y = Yes, N = No) ').lower()

        def action1():
            today = datetime.today().date()
            print('\nToday: {:}'.format(today))
            print('Are There Any Orders You have To Activate Today?\n')
            self.__OrderService.print_out_future_orders()  # Print Out All The Future Orders
            print("-"*80)
            loop = True
            while loop:
                print('\nWhat Kind Of Car Do You Want? (M = Mini car, S = Station car, J = Jeep')
                car_choice = input('Choose A Category: ').lower()
                if car_choice == 'm':
                    print("-"*80)
                    car_choice = 'Mini Car'
                    print('\nThese Mini Cars Are Available:\n')
                    self.__OrderService.pick_a_category(car_choice)
                    loop = False
                    #break
                elif car_choice == 's':
                    print("-"*80)
                    car_choice = 'Station Car'
                    print('\nThese Station Cars Are Available:\n')
                    self.__OrderService.pick_a_category(car_choice)
                    loop = False
                    #break
                elif car_choice == 'j':
                    print("-"*80)
                    car_choice = 'Jeep'
                    print('\nThese Jeeps Are Available:\n')
                    self.__OrderService.pick_a_category(car_choice)
                    loop = False
                    #break
                else:
                    print('Invalid Input, Try Again!\n')
            print("-"*80)
            SSN_input = input('Enter The SSN Of The Person Who Is Putting In An Order: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            self.__OrderService.remove_from_future_orders(SSN)
            licence_Plate = input('\nEnter The Licence Plate Of The Car: ').upper()
            isFound = self.__OrderService.check_Car(licence_Plate)
            while not isFound:
                print("Car Not Found, Please Try Again!")
                licence_Plate = input('Enter The Licence Plate Of The Car: ').upper()
                isFound = self.__OrderService.check_Car(licence_Plate)
            rent_year = int(input('\nEnter Rent Year: '))
            car_rent_year = self.__OrderService.check_year(rent_year)
            rent_month = int(input('Enter Rent Month: '))
            car_rent_month = self.__OrderService.check_month(rent_month)
            rent_day = int(input('Enter Rent Day: '))
            car_rent_day = self.__OrderService.check_days(rent_day)
            return_year = int(input('\nEnter Return Year: '))
            car_return_year = self.__OrderService.check_year(return_year)
            return_month = int(input('Enter Return Month: '))
            car_return_month = self.__OrderService.check_month(return_month)
            return_day = int(input('Enter Return Day: '))
            car_return_day = self.__OrderService.check_days(return_day)
            loop = True
            while loop:
                if car_return_day == car_rent_day and car_return_month == car_rent_month:
                    print("\nSorry You Can't Rent For Only One Day! Please Try Again\n")
                    car_return_month = int(input('Enter Return Month: '))
                    car_return_month = self.__OrderService.check_month(return_month)
                    car_return_day = int(input('Enter Return Day: '))
                    car_return_day = self.__OrderService.check_days(return_day)
                else:
                    loop = False
            extra_insurance = input('\nDo You Want Extra Insurance: (Y = Yes, N = No) ').lower()
            if extra_insurance == 'y':
                print('\nWe Need Your Credit Card Number Please\n')
                credit_card = input('Enter Your Credit Card Number: ')
                while len(credit_card) != 16:
                    print('Invalid Input, Try Again! (only 16 digits)\n')
                    credit_card = input('Enter Your Credit Card Number:')
            while extra_insurance not in ['y', 'n']:
                print('Invalid Input, Try Again!')
                extra_insurance = input('\nDo You Want Extra Insurance: (Y = Yes, N = No) ').lower()
            payment = input('\nAre You Paying With A Card Or Cash: (1 = Card, 2 = Cash): ')
            if payment == '1':
                cardholder = input("\nEnter The Cardholder's Name: ")
                card = input('Enter Your Card Number: ')
                while len(card) != 16:
                    print('Invalid Input, Try Again! (only 16 digits)\n')
                    card = input('Enter Your Card Number: ')
                exp_date = input('Enter The Expiration Date: (mm-yy) ')
                sec_num = input('Enter The Security Number: ')
                print('\nPayment Completed!')
            if payment == '2':
                print('Payment Completed!')
            self.__OrderService.put_in_an_order(SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day,
                                                car_return_year, car_return_month, car_return_day, extra_insurance)
            print('\nOrder Added!')

        def action2():
            print("-"*80)
            SSN_input = input('Enter The SSN: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            Name = input('Enter Name: ')
            category_inp = input('Enter The Category (M = Mini Car, S = Station Car, J = Jeep): ').lower()
            Category = self.__CarService.check_Category(category_inp)
            rent_year = int(input('Enter Rent Year: '))
            car_rent_year = self.__OrderService.check_year(rent_year)
            rent_month = int(input('Enter Rent Month: '))
            car_rent_month = self.__OrderService.check_month(rent_month)
            rent_day = int(input('Enter Rent Day: '))
            car_rent_day = self.__OrderService.check_days(rent_day)
            print("-"*80)
            return_year = int(input('Enter Return Year: '))
            car_return_year = self.__OrderService.check_year(return_year)
            return_month = int(input('Enter Return Month: '))
            car_return_month = self.__OrderService.check_month(return_month)
            return_day = int(input('Enter Return Day: '))
            car_return_day = self.__OrderService.check_days(return_day)
            loop = True
            while loop:
                if car_return_day == car_rent_day and car_return_month == car_rent_month:
                    print("\nSorry You Can't Rent For Only One Day! Please Try Again\n")
                    car_return_month = int(input('Enter Return Month: '))
                    car_return_day = int(input('Enter Return Day: '))
                else:
                    loop = False
            extra_insurance = input('Do You Want Extra Insurance: (Y = Yes, N = No) ').lower()
            while extra_insurance not in ['y', 'n']:
                print('Invalid Input, Try Again!')
                extra_insurance = input('\nDo You Want Extra Insurance: (Y = Yes, N = No) ').lower()
            self.__OrderService.put_in_future_order(SSN, Name, Category, car_rent_year, car_rent_month, car_rent_day, car_return_year, 
                                                    car_return_month,car_return_day, extra_insurance)
            print("\nOrder Added!")

        def main():
            new_Or_Old()
            print_Choices()
            action = ""
            while action not in ["1", "2"]:
                action = input('Choose Command: ').lower()
                # Press 1 to Put In Order
                if action == '1':
                    action1()
                # Press 2 to Put In Future Order
                elif action == '2':
                    action2()
                else:
                    print('\nInvalid Input, Try Again!\n')

        main()

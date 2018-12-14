from services.OrderService import OrderService
from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Order import Order
from models.Customer import Customer
from repo.CustomerOptions import CustomerOptions
from ui.Put_In_Order_UI import Put_In_Order_UI
from datetime import datetime


class Order_UI:

    def __init__(self):
        self.__OrderService = OrderService()
        self.__CarService = CarService()
        self.__Customer = CustomerOptions()
        self.__CustomerService = CustomerService()

    def Order_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with orders in the system '''
            print('{:<40}{:>40}'.format('The Car Rental', 'F To Go to Frontpage'))
            print('-'*80)
            print("{:^80}".format('ORDERS'))
            print('-'*80)
            print('Press 1 to Put In Order')
            print('Press 2 to Cancel Order')
            print('Press 3 to Look Up Order')
            print('Press 4 to Change Order')
            print('Press 5 to Return Car')
            print('Press F to Go To Frontpage\n')

        # Press 2 to Cancel Order
        def action2():
            print("-"*80)
            SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            print()
            # isFound iterates through the file and if there is not match it will allow the user to try again or quit
            isFound = self.__OrderService.check_Order(SSN)
            if isFound:
                self.__OrderService.cancel_Order(SSN)
                print('Order Canceled!')
            while not isFound:
                again = input("Order Not Found! (1 = Try Again, 2 = to Quit)")
                if again == '1':
                    SSN_input = input('\nEnter The SSN Of The Person Who Put In Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    print()
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    if isFound:
                        self.__OrderService.cancel_Order(SSN)
                        print('Order Canceled!')
                else:
                    print('Quitting..')
                    break

        # Press 3 to Look Up Order
        def action3():
            print("-"*80)
            SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            print()
            # isFound iterates through the file and if there is not match it will allow the user to try again or quit
            isFound = self.__OrderService.check_Order(SSN)
            if isFound:
                print()
                self.__OrderService.look_up_order(SSN)
            while not isFound:
                again = input("Order Not Found! (1 = Try Again, 2 = to Quit) ")
                if again == '1':
                    SSN_input = input('Enter The SSN Of The Person Who Put In Order: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    if isFound:
                        print()
                        self.__OrderService.look_up_order(SSN)
                else:
                    print('Quitting..')
                    break

        # Press 4 to Change Order
        def action4():
            print("-"*80)
            SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            # isFound iterates through the file and if there is not match it will allow the user to try again
            isFound = self.__CustomerService.check_Costumer(SSN)
            while not isFound:
                print("\nOrder Not Found! Please Try Again\n")
                SSN_input = input('Enter The SSN Of The Person Who Put In The Order: ')
                SSN = self.__CustomerService.check_SSN(SSN_input)
                isFound = self.__CustomerService.check_Costumer(SSN)
            print()
            self.__OrderService.look_up_order(SSN)
            print('\n\nPress 1 To Change Rent Date')
            print('Press 2 To Change Return Date')
            print('Press 3 To Change Extra Insurance (Y = Yes, N = No)\n')
            choice = input('Enter Choice: ')
            while choice not in ['1', '2', '3']:
                print('Invalid Input, Try Again!\n')
                choice = input('Enter Choice: ')
            if choice == '1' or choice == '2':
                print('Put In The Date In The Format yyyy-mm-dd\n')
            changes = input('Enter New Info: ').lower()
            self.__OrderService.change_Order(SSN, choice, changes)
            print('\nOrder Changed!')

        # Press 5 to Return Car
        def action5():
            print("-"*80)
            print('Return Car: \n')
            self.__OrderService.print_orders()
            plate = input('\nEnter The Licence Plate Of The Car You Want To Return: ')
            plate = plate.upper()
            self.__OrderService.return_car(plate)
            print('\nCar Returned!')

        def main():
            print_Choices()
            action = ""
            while action not in ["1", "2", "3", "4", "5", "F"]:
                action = input('Choose Command: ').lower()
                if action == '1':
                    # Press 1 to Put in order
                    ui = Put_In_Order_UI()
                    ui.Put_In_Order_Menu()
                # Press 2 to Cancel Order
                elif action == '2':
                    action2()
                # Press 3 to Look Up Order
                elif action == '3':
                    action3()
                # Press 4 to Change Order
                elif action == '4':
                    action4()
                # Press 5 to Return Car'
                elif action == '5':
                    action5()
                # Press F to Go To Frontpage
                elif action == 'f':
                    break
                else:
                    print("Invalid Input, Try Again!")

        main()

from services.CustomerService import CustomerService
from services.CarService import CarService
from services.OrderService import OrderService
from ui.Customer_UI import Customer_UI
from ui.Car_UI import Car_UI
from ui.Order_UI import Order_UI
from ui.Put_In_Order_UI import Put_In_Order_UI

from datetime import datetime


class Front_Page_UI:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.__OrderService = OrderService()

    def main_Menu(self):
        def print_Frontpage():
            print('\n\n\n{:<40}{:>40}'.format('The Car Rental', 'Front page'))
            print('-'*80)
            today = datetime.today().date()
            print("{:^80}".format('HELLO'))
            print('-'*80)
            print('Today is {:}'.format(today))
            print('\n\nPress 1 For Customers')
            print('Press 2 For Cars')
            print('Press 3 For Orders')
            print('Press Q To Quit\n')

        def main():
            action = ''
            while (action != 'q'):
                print_Frontpage()
                action = input('Choose Command: ').lower()
                print()
                # Press 1 for Customers
                if action == '1':
                    ui = Customer_UI()
                    ui.customer_Menu()
                # Press 2 for Cars
                elif action == '2':
                    ui = Car_UI()
                    ui.car_Menu()
                # Press 3 for Orders
                elif action == '3':
                    ui = Order_UI()
                    ui.Order_Menu()
                # Press q to Quit
                elif action == 'q':
                    print("Exiting Program. Goodbye !\n")
                else:
                    print('Invalid Input, Try Again!\n')

        main()

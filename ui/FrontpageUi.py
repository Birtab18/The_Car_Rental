from services.CustomerService import CustomerService
from services.CarService import CarService
from services.OrderService import OrderService
from ui.CustomerUi import Customer_Page
from ui.CarUi import Car_Page
from ui.OrderUi import Order_Page


class Front_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.__OrderService = OrderService()

    def main_Menu(self):

        def print_Frontpage():
            print('{:40}{:8}'.format('The Car Rental', 'Front page'))
            print('-'*50)
            print("{:>26}".format('Hello'))
            print('-'*50)
            print('Press 1 for Customers')
            print('Press 2 for Cars')
            print('Press 3 for Orders')
            print('Press q to Quit')
            print()

        action = ''
        while (action != 'q'):
            print_Frontpage()
            action = input('Choose command: ').lower()
            print()
            if action == '1':
                ui = Customer_Page()
                ui.customer_Menu()

            elif action == '2':
                ui = Car_Page()
                ui.car_Menu()
            
            elif action == '3':
                ui = Order_Page()
                ui.Order_Menu()

            elif action == 'q':
                print("Goodbye !")
            
            else:
                print('Invalid input, try again!')
                print()

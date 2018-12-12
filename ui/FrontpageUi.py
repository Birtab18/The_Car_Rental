from services.CustomerService import CustomerService
from services.CarService import CarService
from services.OrderService import OrderService
from ui.CustomerUI import Customer_UI
from ui.CarUI import Car_UI
from ui.OrderUI import Order_UI


class Front_Page_UI:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.__OrderService = OrderService()

    def main_Menu(self):
        def print_Frontpage():
            print('\n\n\n{:<30}{:>30}'.format('The Car Rental', 'Front page'))
            print('-'*60)
            print("{:^60}".format('HELLO'))
            print('-'*60)
            print('Press 1 for Customers')
            print('Press 2 for Cars')
            print('Press 3 for Orders')
            print('Press q to Quit\n')

        action = ''
        while (action != 'q'):
            print_Frontpage()
            action = input('Choose command: ').lower()
            print()
            if action == '1':
                ui = Customer_UI()
                ui.customer_Menu()

            elif action == '2':
                ui = Car_UI()
                ui.car_Menu()
            
            elif action == '3':
                ui = Order_UI()
                ui.Order_Menu()

            elif action == 'q':
                print("Exiting Program. Goodbye !\n")
            
            else:
                print('Invalid input, try again!\n')

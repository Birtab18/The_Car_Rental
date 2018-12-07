from services.CustomerService import CustomerService
from services.CarService import CarService
from ui.CarUi import Car_Page
from ui.CustomerUi import Customer_Page


class Front_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()

    def main_Menu(self):

        def print_Frontpage():
            print('{:40}{:8}'.format('The Car Rental', 'Front page'))
            print('-'*50)
            print("{:>26}".format('Hello'))
            print('-'*50)
            print('Press 1 for Customer')
            print('Press 2 for Car')
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

            elif action == 'q':
                print("Goodbye !")
                pass  # quit
            else:
                print('Invalid input, try again!')

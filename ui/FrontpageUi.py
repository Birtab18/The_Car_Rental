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
            print()
            print()
            print()
            print()
            print('{0:40}{1}'.format('The Car Rental', 'Front page'))
            print('-'*50)
            print("{0:>26}".format('Hello'))
            print('-'*50)
            print('Press 1 for Customer')
            print('Press 2 for Car')
            print('Press q to Quit')

        action = ''
        while (action != 'q'):


<< << << < HEAD
  print_Frontpage()  # forsida
== == == =
  print_Frontpage()
>>>>>> > b6defbf6ef5d8e730743065c595284e209ef390a
  action = input('Choose command: ').lower()
   if action == '1':
        ui = Customer_Page()
        ui.customer_Menu()

    elif action == '2':
        ui = Car_Page()
        ui.car_Menu()

    elif action == 'q':
        print("Goodbye !")
        pass  # quit

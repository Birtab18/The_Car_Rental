from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Customer import Customer
from models.Car import Car


class Frontpage:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()

    def main_menu(self):

        def front_Page():
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

        def customer_Page():
            print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
            print('-'*50)
            print("{0:>26}".format('Customers'))
            print('-'*50)
            print('Press 1 to Sign Up New Customer ')
            print('Press 2 to Delete Customer')
            print('Press 3 to Look Up Customer')
            print('Press 4 to Change Information About A Customer')
            print('Press q to Quit')

        def car_Page():
            print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
            print('-'*50)
            print("{0:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Mark Car As Available For Rent')
            print('Press 2 to Mark Car As Not Available For Rent')
            print('Press 3 to Put In An Order')
            print('Press 4 to Cancel Order')
            print('Press 5 to Look Up Order')
            print('Press 6 to Change Order')
            print('Press 7 to Show Cars Availability')  # True or False
            print('Press 8 to Show Price List')
            print('Press 9 to Add A New Car To The Car Rental')
            print('Press 10 to Change The Price List')
            print('Press q to Quit')

        # def sign_Up():

        action = ''
        while (action != 'q'):
            front_Page()  # forsida
            action = input('Choose command: ').lower()
            if action == '1':
                customer_Page()  # customer valmyndin
                action_Cust = input('Choose command: ').lower()
                if action_Cust == '1':
                    print("-"*15)
                    print("New customer:")
                    name = input('Enter a name: ')
                    socialnumber = input('Enter a SSN number: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter an email: ')
                    new_Costumer = Customer(name, socialnumber, phonenumber, email)
                    self.__CustomerService.add_customer(new_Costumer)
                elif action_Cust == '2':
                    costumer = self.__CustomerService.get_costumer()
                elif action_Cust == '3':
                    pass
                elif action_Cust == '4':
                    pass
                elif action_Cust == 'b':
                    pass
                else:
                    print("Invalid input, try again!")
                    continue

            elif action == '2':
                car_Page()  # bila valmynd
                action_Car = input('Choose command: ').lower()
                if action_Car == '1':
                    print("mark car")
                    pass
                elif action_Car == '2':
                    pass
                elif action_Car == '3':
                    pass
                elif action_Car == '4':
                    pass
                elif action_Car == '5':
                    pass
                elif action_Car == '6':
                    pass
                elif action_Car == '7':
                    pass
                elif action_Car == '8':
                    pass
                elif action_Car == '9':
                    print("-"*15)
                    print("New customer:")
                    manufacturer = input('Enter The Manufacturer: ')
                    the_Type = input('Enter The Type: ')
                    transmission = input('Stick Shift Or Manual?: ')
                    color = input('Enter The Color: ')
                    price = input('Enter Price: ')
                    #status = input('Enter Status: ')
                    new_Car = Car(manufacturer, the_Type, transmission, color, price)
                    self.__CarService.add_car(new_Car)
                elif action_Car == '10':
                    pass
                elif action_Car == 'q':
                    pass
                else:
                    print("Invalid input, try again!")
                    continue

            elif action == 'q':
                print("Goodbye !")
                pass  # quit

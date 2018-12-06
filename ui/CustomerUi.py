from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Customer import Customer
from models.Car import Car


class Customer_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()

    def customer_Menu(self):

        def print_Choices():
            print('{0:40}{1}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{0:>26}".format('Customers'))
            print('-'*50)
            print('Press 1 to Sign Up New Customer ')
            print('Press 2 to Delete Customer')
            print('Press 3 to Look Up Customer')
            print('Press 4 to Change Information About A Customer')
            print('Press b to go to Frontpage')

        def main():
            print_Choices()
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
                self.__CustomerService.delete_customer()
            elif action_Cust == '3':
                self.__CustomerService.get_costumer()
            elif action_Cust == '4':
                pass
            elif action_Cust == 'b':
                print_Frontpage()
            else:
                print("Invalid input, try again!")

        main()

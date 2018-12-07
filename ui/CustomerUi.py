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
            print('Press b to Go To Frontpage')

        def main():
            print_Choices()
            action_Cust = input('Choose command: ').lower()
            if action_Cust == '1':
                print("-"*15)
                print("New customer:")
                socialnumber = input('Enter a SSN number: ')
                name = input('Enter a name: ')
                phonenumber = input('Enter a phonenumber: ')
                email = input('Enter an email: ')
                new_Costumer = Customer(socialnumber, name, phonenumber, email)
                self.__CustomerService.add_customer(new_Costumer)
            
            elif action_Cust == '2':
                person_delete = input('Enter The SSN Of The Person You Want To Delete: ')
                self.__CustomerService.delete_customer(person_delete)
            
            elif action_Cust == '3':
                person_change = input('Enter The SSN Of The Person You Want To Look Up: ')
                self.__CustomerService.look_up_customer(person_change)
            
            elif action_Cust == '4':
                print()
                print('press 1 to change SSN')
                print('Press 2 to change Name')
                print('Press 3 to change Phone Number')
                print('Press 4 to change Email')
                print()
                ssn_number = input('Enter the SSN of the person you want to change: ')
                num = input('Enter Choice: ')
                changes = input('Enter New Info: ')
                self.__CustomerService.Change_Information(ssn_number, num, changes)
            
            elif action_Cust == 'b':
                pass
                #print_Frontpage()
            
            else:
                print("Invalid input, try again!")
        
        main()
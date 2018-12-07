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
            print('{:<30}{:>20}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{:>26}".format('Customers'))
            print('-'*50)
            print('Press 1 to Sign Up New Customer ')
            print('Press 2 to Delete Customer')
            print('Press 3 to Look Up Customer')
            print('Press 4 to Change Information About A Customer')
            print('Press b to Go To Frontpage')
            print()

        def main():
            print_Choices()
            action_Cust = input('Choose command: ').lower()
            print()
            if action_Cust == '1':
                print("-"*15)
                print("New customer:")
                socialnumber = input('Enter a SSN number: ')
                name = input('Enter a name: ')
                phonenumber = input('Enter a phonenumber: ')
                email = input('Enter an email: ')
                new_Costumer = Customer(socialnumber, name, phonenumber, email)
                self.__CustomerService.add_customer(new_Costumer)
                print()
            
            elif action_Cust == '2':
                person_delete = input('Enter The SSN Of The Person You Want To Delete: ')
                self.__CustomerService.delete_customer(person_delete)
            
            elif action_Cust == '3':
                person_Look_Up = input('Enter The SSN Of The Person You Want To Look Up: ')
                self.__CustomerService.look_up_customer(person_Look_Up)
            
            elif action_Cust == '4':
                print()
                print('press 1 to Change SSN')
                print('Press 2 to Change Name')
                print('Press 3 to Change Phone Number')
                print('Press 4 to Change Email')
                print()
                ssn_number = input('Enter The SSN Of The Person You Want To Change: ')
                choice = input('Enter Choice: ')
                changes = input('Enter New Info: ')
                self.__CustomerService.Change_Information(ssn_number, choice, changes)
            
            elif action_Cust == 'b':
                pass
                #print_Frontpage()
            
            else:
                print("Invalid input, try again!")
        
        main()
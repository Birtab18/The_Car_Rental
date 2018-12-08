from services.CustomerService import CustomerService
from models.Customer import Customer
# from ui.FrontpageUi import Front_Page

class Customer_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()

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
            print('Press F to Go To Frontpage')
            print()

        def main():
            print_Choices()
            print()
            action = ""
            while action not in ["1","2","3","4","F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*15)
                    print("New customer:")
                    socialnumber = input('Enter a SSN number: ')
                    name = input('Enter a name: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter an email: ')
                    new_Costumer = Customer(socialnumber, name, phonenumber, email)
                    self.__CustomerService.add_customer(new_Costumer)
                    print()
                
                elif action == '2':
                    person_delete = input('Enter The SSN Of The Person You Want To Delete: ')
                    self.__CustomerService.delete_customer(person_delete)
                
                elif action == '3':
                    person_Look_Up = input('Enter The SSN Of The Person You Want To Look Up: ')
                    self.__CustomerService.look_up_customer(person_Look_Up)
                    print()
                
                elif action == '4':
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
                
                elif action == 'f':
                    # ui = Front_Page()
                    # ui.main_Menu()
                    pass
                
                else:
                    print("Invalid input, try again!")
                    print()
                
        main()
from services.CustomerService import CustomerService
from models.Customer import Customer


class Customer_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()

    def customer_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with customers in the system '''
            print('{:<30}{:>20}'.format('The Car Rental', 'F To Go to Frontpage'))
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
            action = ""
            while action not in ["1","2","3","4","F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*15)
                    print("New customer:")
                    SSN = input('Enter A SSN: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)\n')
                        SSN = input('Enter A SSN: ')
                    name = input('Enter a name: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter an email: ')
                    new_Costumer = Customer(SSN, name, phonenumber, email)
                    self.__CustomerService.add_customer(new_Costumer)
                    print('\nCustomer Signed!\n\n')
                
                elif action == '2':
                    print("-"*15)
                    SSN = input('Enter The SSN Of The Person You Want To Delete: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)\n')
                        SSN = input('Enter The SSN Of The Person You Want To Delete: ')
                    self.__CustomerService.delete_customer(SSN)
                    print('\nCustomer Deleted!\n\n')
                
                elif action == '3':
                    print("-"*15)
                    SSN = input('Enter The SSN Of The Person You Want To Look Up: ')
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)\n')
                        SSN = input('Enter The SSN Of The Person You Want To Look Up: ')
                    self.__CustomerService.look_up_customer(SSN)
                    print()
                
                elif action == '4':
                    print("-"*15)
                    SSN = input('Enter The SSN Of The Person You Want To Change: ')    
                    print()
                    print('press 1 to Change SSN')
                    print('Press 2 to Change Name')
                    print('Press 3 to Change Phone Number')
                    print('Press 4 to Change Email')
                    print()
                    while len(SSN) != 10:
                        print('Error! Please Input A Valid SSN (only 10 digits)\n')
                        SSN = input('Enter The SSN Of The Person You Want To Change: ')
                    choice = input('Enter Choice: ')
                    changes = input('Enter New Info: ')
                    self.__CustomerService.Change_Information(SSN, choice, changes)
                    print('\nCustomer Info Changed!\n\n')
                
                elif action == 'f':
                    break
                
                else:
                    print("Invalid input, try again!")
        
        main()

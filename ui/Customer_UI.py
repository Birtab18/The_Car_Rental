from services.CustomerService import CustomerService
from models.Customer import Customer


class Customer_UI:
    def __init__(self):
        self.__CustomerService = CustomerService()

    def customer_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with customers in the system '''
            print('{:<30}{:>30}'.format('The Car Rental', 'F To Go to Frontpage'))
            print('-'*60)
            print("{:^60}".format('CUSTOMERS'))
            print('-'*60)
            print('Press 1 to Sign Up New Customer ')
            print('Press 2 to Delete Customer')
            print('Press 3 to Look Up Customer')
            print('Press 4 to Change Information About A Customer')
            print('Press F to Go To Frontpage\n')

        def main():
            print_Choices()
            action = ""
            while action not in ["1","2","3","4","F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*60)
                    print("New customer:")
                    SSN_input = input('Enter The SSN Of The Person You Want To Sign Up: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isfound = self.__CustomerService.check_Costumer(SSN)
                    if isfound:
                        print('\nCustomer Already Exists!')
                    else:
                        name = input('Enter A Name: ')
                        phonenumber_input = input('Enter A Phone Number: ')
                        phonenumber = self.__CustomerService.check_Phonenumber(phonenumber_input)
                        email = input('Enter An Email: ')
                        new_Costumer = Customer(SSN, name, phonenumber, email)
                        self.__CustomerService.add_customer(new_Costumer)
                        print('\nCustomer Signed!')

                elif action == '2':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person You Want To Delete: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    if isFound:
                        self.__CustomerService.delete_customer(SSN)
                        print('\nCustomer Deleted!')
                    while not isFound:
                        again = input("Costumer Not Found! Press 1 to Try Again, Press 2 to Quit: ")
                        if again == '1':
                            SSN_input = input('\nEnter The SSN Of The Person You Want To Delete: ')
                            SSN = self.__CustomerService.check_SSN(SSN_input)
                            isFound = self.__CustomerService.check_Costumer(SSN)
                            if isFound:
                                self.__CustomerService.delete_customer(SSN)
                                print('\nCustomer Deleted!')
                        else:
                            print('\nQuitting..')
                            break


                elif action == '3':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person You Want To Look Up: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    if isFound:
                        self.__CustomerService.look_up_customer(SSN)
                    while not isFound:
                        again = input("Costumer Not Found! Press 1 to Try Again, Press 2 to Quit: ")
                        if again == '1':
                            SSN_input = input('\nEnter The SSN Of The Person You Want To Look Up: ')
                            SSN = self.__CustomerService.check_SSN(SSN_input)
                            isFound = self.__CustomerService.check_Costumer(SSN)
                            if isFound:
                                self.__CustomerService.look_up_customer(SSN)
                        else:
                            print('\nQuitting..\n\n')
                            break

                elif action == '4':
                    print("-"*60)
                    SSN_input = input('Enter The SSN Of The Person You Want To Change: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    while not isFound:
                        print("\nCostumer Not Found! Please Try Again")
                        SSN_input = input('\nEnter The SSN Of The Person You Want To Change: ')
                        SSN = self.__CustomerService.check_SSN(SSN_input)
                        isFound = self.__CustomerService.check_Costumer(SSN)
                    print('\npress 1 to Change The SSN')
                    print('Press 2 to Change The Name')
                    print('Press 3 to Change The Phone Number')
                    print('Press 4 to Change The Email\n')
                    choice_input = input('Enter Choice: ')
                    choice = self.__CustomerService.check_Choice(choice_input)
                    changes = input('Enter New Info: ')
                    if choice == '1':
                        changes = self.__CustomerService.check_SSN(changes)
                    elif choice == '3':
                        changes = self.__CustomerService.check_Phonenumber(changes)
                    self.__CustomerService.Change_Information(SSN, choice, changes)
                    print('\nCustomer Info Changed!')
                
                elif action == 'f':
                    break
                
                else:
                    print("Invalid input, try again!\n")
                
        main()

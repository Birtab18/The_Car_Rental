from services.CustomerService import CustomerService
from models.Customer import Customer


class Customer_UI:
    def __init__(self):
        self.__CustomerService = CustomerService()

    def customer_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with customers in the system '''
            print('{:<40}{:>40}'.format('The Car Rental', 'F To Go To Frontpage'))
            print('-'*80)
            print("{:^80}".format('CUSTOMERS'))
            print('-'*80)
            print('Press 1 To Sign Up New Customer ')
            print('Press 2 To Delete Customer')
            print('Press 3 To Look Up Customer')
            print('Press 4 To Change Information About A Customer')
            print('Press F To Go To Frontpage\n')

        def action1():
            print("-"*80)
            print("New customer:")
            SSN_input = input('Enter The SSN Of The Person You Want To Sign Up: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            # isFound iterates through the file and if there is a match, it will let you know that the customer already exists
            isfound = self.__CustomerService.check_Costumer(SSN)
            if isfound:
                print('\nCustomer Already Exists!')
            else:
                name = input('Enter A Name: ')
                phonenumber_input = input('Enter A Phone Number: ')
                phonenumber = self.__CustomerService.check_Phonenumber(
                    phonenumber_input)
                email = input('Enter An Email: ')
                new_Costumer = Customer(SSN, name, phonenumber, email)
                self.__CustomerService.add_customer(new_Costumer)
                print('\nCustomer Signed!')

        def action2():
            print("-"*80)
            SSN_input = input(
                'Enter The SSN Of The Person You Want To Delete: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            # isFound iterates through the file and if there is not match it will allow the user to try again or quit
            isFound = self.__CustomerService.check_Costumer(SSN)
            if isFound:
                self.__CustomerService.delete_customer(SSN)
                print('\nCustomer Deleted!')
            while not isFound:
                again = input("\nCostumer Not Found! (1 = Try Again, 2 = Quit) ")
                if again == '1':
                    SSN_input = input('\nEnter The SSN Of The Person You Want To Delete: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(
                        SSN)
                    if isFound:
                        self.__CustomerService.delete_customer(SSN)
                        print('\nCustomer Deleted!')
                else:
                    print('\nQuitting..')
                    break

        def action3():
            print("-"*80)
            SSN_input = input(
                'Enter The SSN Of The Person You Want To Look Up: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            # isFound iterates through the file and if there is not match it will allow the user to try again or quit
            isFound = self.__CustomerService.check_Costumer(SSN)
            if isFound:
                print()
                print()
                self.__CustomerService.look_up_customer(SSN)
            while not isFound:
                again = input("Costumer Not Found! (1 = Try Again, 2 = Quit) ")
                if again == '1':
                    SSN_input = input('\nEnter The SSN Of The Person You Want To Look Up: ')
                    SSN = self.__CustomerService.check_SSN(SSN_input)
                    isFound = self.__CustomerService.check_Costumer(SSN)
                    if isFound:
                        print()
                        print()
                        self.__CustomerService.look_up_customer(SSN)
                else:
                    print('\nQuitting..')
                    break

        def action4():
            print("-"*80)
            SSN_input = input('Enter The SSN Of The Person You Want To Change: ')
            SSN = self.__CustomerService.check_SSN(SSN_input)
            # isFound iterates through the file and if there is not match it will allow the user to try again
            isFound = self.__CustomerService.check_Costumer(SSN)
            print()
            print()
            self.__CustomerService.look_up_customer(SSN)
            while not isFound:
                print("Costumer Not Found! Please Try Again")
                SSN_input = input('\nEnter The SSN Of The Person You Want To Change: ')
                SSN = self.__CustomerService.check_SSN(SSN_input)
                isFound = self.__CustomerService.check_Costumer(SSN)
                print()
                print()
                self.__CustomerService.look_up_customer(SSN)
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

        def main():
            print_Choices()
            action = ""
            while action not in ["1", "2", "3", "4", "F"]:
                action = input('Choose Command: ').lower()
                # Press 1 to Sign Up New Customer
                if action == '1':
                    action1()
                # Press 2 to Delete Customer
                elif action == '2':
                    action2()
                # Press 3 to Look Up Customer
                elif action == '3':
                    action3()
                # Press 4 to Change Information About A Customer
                elif action == '4':
                    action4()
                # Press F to Go To Frontpage
                elif action == 'f':
                    break
                else:
                    print("Invalid Input, Try Again!\n")

        main()

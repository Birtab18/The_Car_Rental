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
<<<<<<< HEAD
                self.__CustomerService.Change_Information()
=======
                person_Change = input("Enter The SSN Of The Person To Change It's Info: ")
                the_Change = input('What Do You Want To Change? (1 = SSN, 2 = Name, 3 = Phone Number, 4 = Email) ')
                new_Info = input('Enter The New Info: ')
                self.__CustomerService.change_Customer_Info(person_Change, the_Change, new_Info)
>>>>>>> 6e77566ff7b3be8e7df1711349fc98ef39bb2f1a
            
            elif action_Cust == 'b':
                pass
                #print_Frontpage()
            
            else:
                print("Invalid input, try again!")

        main()



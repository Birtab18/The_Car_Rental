from services.doublechecking import Checking2
from services.vidskiptavinir import Customer

class Frontpage:
    def __init__(self):
        self.__customer_main = Checking2
        

    def main_menu(self):
        action = ''
        while (action !='q'):
            print('Press 1 for Customer')
            print('Press 2 for Car')

            action = input('Choose command: ').lower()

            if action =='1':
                print('Press 1 to Sign Up New Customer ')
                print('Press 2 to Delete Customer')
                print('Press 3 to Look Up Customer')
                print('Press 4 to Change Information About A Customer')
                print('Press q to Quit')
                action_Cust = input('Choose command: ').lower()

                if action_Cust == '1':
                    name = input('Enter a name: ')
                    socialnumber = input('Enter a SSN number: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter an email: ')
                    new_costumer = Customer(name, socialnumber, phonenumber,email)
                    self.__customer_main.add_customer(new_costumer)
                elif action_Cust == '2':
                    costumer = self.__customer_main.get_costumer()
                elif action_Cust == '3':
                    pass
                elif action_Cust == '4':
                    pass
                else: 
                    pass #quit

            elif action == '2':
                print('Press 1 to Set a car free')
                print('Press 2 to set a car in rental')
                print('Press 3 to Put in an order')
                print('Press 4 to Delete order')
                print('Press 5 to Look up a order')
                print('Press 6 to Change a order')
                print('Press 7 to showing cars status')
                print('Press 8 to showing how much each car cost')
                print('Press q to Quit')
                action_Car = input('Choose command: ').lower()

                if action_Car == '1':
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
                else:
                    pass #quit


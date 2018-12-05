from checking.doublechecking import Checking2
from upplysingar.vidskiptavinir import Customer

class Frontpage:
    def __init__(self):
        self.__customer_main = Checking2

    def main_menu(self):
        action = ''
        while (action !='q'):
            print('Press 1 for Customer')
            print('Press 2 for Vehicle')

            action = input('Choose option: ').lower()

            if action =='1':
                print('Press 1 for Sign Customer up')
                print('Press 2 to Delete Customer')
                print('Press 3 for Look up Cusoumer')
                print('Press 4 for Change information about customer')
                action2= input('Choose option: ').lower()

                if action2 == '1':
                    name = input('Enter a name: ')
                    socialnumber = input('Enter a number: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter a email: ')
                    new_costumer = Customer(name, socialnumber, phonenumber,email)
                    self.__customer_main.add_customer(new_costumer)
                
     
            elif action == '2':
                print('Press 1 for Set a car free')
                print('Press 2 for set a car in rental')
                print('Press 3 for Put in an order')
                print('Press 4 for Delete order')
                print('Press 5 for Look up a order')
                print('Press 6 for Change a order')
                print('Press 7 for showing cars stadus')
                print('Press 8 for showing how much each car cost')



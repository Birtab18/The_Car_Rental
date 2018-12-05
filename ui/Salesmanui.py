from services.doublechecking import Checking2
from services.vidskiptavinir import Customer

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
                print('Press 1 to Sign Up New Customer ')
                print('Press 2 to Delete Customer')
                print('Press 3 to Look Up Customer')
                print('Press 4 to Change Information About A Customer')
                action2= input('Choose option: ').lower()

                if action2 == '1':
                    name = input('Enter a name: ')
                    socialnumber = input('Enter a number: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter email: ')
                    new_costumer = Customer(name, socialnumber, phonenumber,email)
                    self.__customer_main.add_customer(new_costumer)
                elif action2 == '2':
                    costumer = self.__customer_main.get_costumer()

            elif action == '2':
<<<<<<< HEAD
                print('Press 1 for Set a car free')
                print('Press 2 for set a car in rental')
                print('Press 3 for Put in an order')
                print('Press 4 for Delete order')
                print('Press 5 for Look up a order')
                print('Press 6 for Change a order')
                print('Press 7 for showing cars status')
                print('Press 8 for showing how much each car cost')

=======
                print('Press 1 to Set a car free')
                print('Press 2 to Set a car in rental')
                print('Press 3 to Put in an order')
                print('Press 4 to Delete Order')
                print('Press 5 to Look Up A Order')
                print('Press 6 to Change A Order')
                print('Press 7 to Show Cars Status')
                print('Press 8 to Show Price List')


#test
>>>>>>> 0e0aa4b3a234e9ef04b566c740cc466ee2092bc7

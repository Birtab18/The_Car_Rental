from services.OrderService import OrderService
from models.Order import Order


class Order_Page:
    def __init__(self):
        self.__OrderService = OrderService()

    def Order_Menu(self):

        def print_Choices():
            print('{:<30}{:>20}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Put In Order')
            print('Press 2 to Cancel Order') 
            print('Press 3 to Look Up Order')
            print('Press 4 to Change Order')
            print('Press q to Quit')
            print()

        def main():
            print_Choices()
            action = input('Choose command: ').lower()
            if action == '1':
                print("-"*15)
                # new_Or_Old = input(
                #     'Has the customer rented a car from us before? y = Yes, n = No').lower()
                # while new_Or_Old != 'y' or 'n':
                #     if new_Or_Old == 'y':
                #         # go to look up customer
                #         pass
                #     elif new_Or_Old == 'n':
                #         # go to sign up new customer
                #         pass
                #     else:
                #         print('Invalid input, try again!')

                # print("New Order:")
                # licence_Plate = input('Enter The Licence Plate: ')
                # # þurfum að leita upp línunni í cars með þetta nr og taka þær uppl og setja i orders
                # # með uppl um vv
                # # notum daytime moduleinn her?
                # rent_Date = input('Enter The Date Of The Rent: ')
                # # like her daytime?
                # return_Date = input('Enter The Date Of The Return: ')
                # insurance = input('Extra insurance? (Y = Yes, N = No) ')
                # new_Order = Order(the_Customer, the_Car, rent_Date, return_Date, insurance)
                look_up = input('Enter The SSN Of The Person who want to rent a car: ')
                car_id = input('Enter licenche: ')
                a = int(input('Y: '))
                b = int(input('M: '))
                c = int(input('D: '))
                e = int(input('Y: '))
                f = int(input('M: '))
                g = int(input('D: '))
    
                self.__OrderService.put_in_an_order(look_up,car_id,a,b,c,e,f,g)

            elif action == '2':
                ssn = input('Enter The SSN Of The Person Who Put In The Order: ')
                licence_Plate = input('Enter The Licence Plate Of The Car: ')
                self.__OrderService.cancel_Order(ssn, licence_Plate)

            elif action == '3':
                look_Up = input('Enter The Licence Plate Of The Car: ')
                print()
                self.__OrderService.look_up_order(look_Up)
                print()

            elif action == '4':
                print()
                print('press 1 to Change Category (Mini Car, Station Car Or Jeep)')
                print('Press 2 to Change Rent Date')
                print('Press 3 to Change Return Date')
                print('Press 4 to Change Extra Insurance (Y = Yes, N = No')
                print()
                ssn = input('Enter The SSN Of The Person Who Ordered The Car: ')
                choice = input('Enter Choice: ')
                changes = input('Enter New Info: ').lower()
                self.__OrderService.change_Order(ssn, choice, changes)

        main()

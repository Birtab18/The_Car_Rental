from services.CustomerService import CustomerService
from services.CarService import CarService
from services.OrderService import OrderService
from models.Customer import Customer
from models.Car import Car


class Car_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.__OrderService = OrderService()

    def car_Menu(self):

        def print_Choices():
            print('{:<30}{:>20}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Show Available Cars')
            print('Press 2 to Show Unavailable Cars')
            print('Press 3 to Put In Order')
            print('Press 4 to Cancel Order')
            print('Press 5 to Look Up Order')
            print('Press 6 to Change Order')
            print('Press 7 to Show Price List')
            print('Press 8 to Add A New Car To The Car Rental')
            print('Press q to Quit')
            print()


        def main():
            print_Choices()
            action_Car = input('Choose command: ').lower()
            print()
            if action_Car == '1':
                print('Available Cars: \n')
                print()
                self.__CarService.available_cars()

            elif action_Car == '2':
                print('Unavailable Cars: \n')
                print()
                self.__CarService.taken_cars()

            elif action_Car == '3':
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

            elif action_Car == '4':
                ssn = input('Enter The SSN Of The Person Who Put In The Order: ')
                licence_Plate = input('Enter The Licence Plate Of The Car: ')
                self.__OrderService.cancel_Order(ssn, licence_Plate)

            elif action_Car == '5':
                look_Up = input('Enter The Licence Plate Of The Car: ')
                print()
                self.__OrderService.look_up_order(look_Up)
                print()
            elif action_Car == '6':
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

            elif action_Car == '7':
                self.__CarService.show_Pricelist()

            elif action_Car == '8':
                print("-"*15)
                print("New customer:")
                licence_Plate = input('Enter The Licence Plate: ').upper()
                category = input(
                    'Enter The Category (Mini Car, Passenger Car, or Jeep): ').lower()
                # þurfum að gera eh svona lykkju
                # category = ''
                # while category != 'm' or 'p' or 'j':
                #     category = input('Enter The Category (M = Mini Car, P = Passenger Car, J = Jeep): ').lower()
                #     if category == 'm':
                #         category = 'Mini Car'
                #     elif category == 'p':
                #         category = 'Passenger Car'
                #     elif category == 'j':
                #         category = 'Jeep'
                #     else:
                #         print("Invalid input, try again!")
                manufacturer = input('Enter The Manufacturer: ')
                the_Type = input('Enter The Type: ')
                transmission = input('Enter The Transmission (Stick Shift or Manual): ').lower()
                # þurfum að gera eh svona lykkju
                # while transmission != 's' or 'm':
                #     if transmission == 's':
                #         transmission == 'Stick Shift'
                #     elif transmission == 'm':
                #         transmission == 'Manual'
                #     else:
                #         print('Invalid input, try again!')
                price = input('Enter Price: ')
                new_Car = Car(licence_Plate, category, manufacturer, the_Type, transmission, price)
                self.__CarService.add_car(new_Car)

            elif action_Car == 'q':
                pass

            else:
                print("Invalid input, try again!")

        main()

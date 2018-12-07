from services.CustomerService import CustomerService
from services.CarService import CarService
from models.Customer import Customer
from models.Car import Car


class Car_Page:
    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()

    def car_Menu(self):

        def print_Choices():
            print('{:<30}{:>20}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Show Available')
            print('Press 2 to Show Unavailable Cars')
            print('Press 3 to Put In Order')
            print('Press 4 to Cancel Order')
            print('Press 5 to Look Up Order')
            print('Press 6 to Change Order')
            print('Press 7')  # True or False
            print('Press 8 to Show Price List')
            print('Press 9 to Add A New Car To The Car Rental')
            print('Press 10 to Change The Price List')  # ekki lagmarkskrafa
            print('Press q to Quit')
            print()


        def main():
            print_Choices()
            action_Car = input('Choose command: ').lower()
            print()
            if action_Car == '1':
                self.__CarService.available_cars()

            elif action_Car == '2':
                self.__CarService.taken_cars()

            elif action_Car == '3':
                print("-"*15)
                new_Or_Old = input(
                    'Has the customer rented a car from us before? y = Yes, n = No').lower()
                while new_Or_Old != 'y' or 'n':
                    if new_Or_Old == 'y':
                        # go to look up customer
                        pass
                    elif new_Or_Old == 'n':
                        # go to sign up new customer
                        pass
                    else:
                        print('Invalid input, try again!')

                print("New Order:")
                licence_Plate = input('Enter The Licence Plate: ')
                # þurfum að leita upp línunni í cars með þetta nr og taka þær uppl og setja i orders
                # með uppl um vv
                # notum daytime moduleinn her?
                rent_Date = input('Enter The Date Of The Rent: ')
                # like her daytime?
                return_Date = input('Enter The Date Of The Return: ')
                insurance = input('Extra insurance? (Y = Yes, N = No) ')
                new_Order = Order(the_Customer, the_Car, rent_Date, return_Date, insurance)
                self.__CarService.add_car(new_Car)

            elif action_Car == '4':
                pass

            elif action_Car == '5':
                pass

            elif action_Car == '6':
                pass

            elif action_Car == '7':
                pass

            elif action_Car == '8':
                self.__CarService.show_Pricelist()

            elif action_Car == '9':
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

            elif action_Car == '10':
                pass

            elif action_Car == 'q':
                pass

            else:
                print("Invalid input, try again!")

        main()

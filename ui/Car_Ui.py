from services.CarService import CarService
from models.Car import Car
from datetime import datetime


class Car_UI:

    def __init__(self):
        self.__CarService = CarService()

    def car_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with cars in the system '''
            print('{:<40}{:>40}'.format('The Car Rental', 'F To Go To Frontpage'))
            print('-'*80)
            print("{:^80}".format('CARS'))
            print('-'*80)
            print('Press 1 To Show Available Cars')
            print('Press 2 To Show Unavailable Cars')
            print('Press 3 To Show Price List')
            print('Press 4 To Add A New Car To The Car Rental')
            print('Press F To Go To Frontpage\n')

        # Press 1 To Show Available Cars
        def action1():
            print("-"*80)
            print('Available Cars: \n')
            self.__CarService.available_cars()

        # Press 2 To Show Unavailable Cars
        def action2():
            print("-"*80)
            print('Unavailable Cars: \n')
            self.__CarService.unavailable_cars()

        # Press 3 To Show Price List
        def action3():
            print("-"*80)
            print()
            self.__CarService.show_Pricelist()

        # Press 4 To Add A New Car To The Car Rental
        def action4():
            print("-"*80)
            print("New Car:")
            licence_Plate = input('Enter The Licence Plate: ')
            licence_Plate = licence_Plate.upper()
            while len(licence_Plate) != 5: # if the licence plate is invalid, the user is asked to try again 
                print('Invalid Input, Try Again!')
                licence_Plate = input('Enter The Licence Plate: ')
                licence_Plate = licence_Plate.upper()
            category_inp = input('Enter The Category (M = Mini Car, S = Station Car, J = Jeep): ').lower()
            category = self.__CarService.check_Category(category_inp)
            manufacturer = input('Enter The Manufacturer: ')
            the_Type = input('Enter The Type: ')
            transmission_inp = input('Enter The Transmission (S = Stick Shift, M = Manual): ').lower()
            transmission = self.__CarService.check_Transmission(transmission_inp)
            price_inp = input('Enter Price: ')
            price = self.__CarService.check_Price(price_inp)
            new_Car = Car(licence_Plate, category,manufacturer, the_Type, transmission, price)
            self.__CarService.add_car(new_Car)
            print('\nCar Added!')

        def main():
            print_Choices()
            action = ""  # so the while loop will start running
            while action not in ["1", "2", "3", "4", "F"]:
                action = input('Choose Command: ').lower()
                # Press 1 to Show Available Cars
                if action == '1':
                    action1()
                # Press 2 to Show Unavailable Cars
                elif action == '2':
                    action2()
                # Press 3 to Show Price List
                elif action == '3':
                    action3()
                # Press 4 to Add A New Car To The Car Rental
                elif action == '4':
                    action4()
                # Press F to Go To Frontpage
                elif action == 'f':
                    break
                else:
                    print("Invalid Input, Try Again!\n")

        main()

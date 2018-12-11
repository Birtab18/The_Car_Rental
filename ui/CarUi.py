from services.CarService import CarService
from models.Car import Car


class Car_Page:
    def __init__(self):
        self.__CarService = CarService()

    def car_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with cars in the system '''
            print('{:<30}{:>30}'.format(
                'The Car Rental', 'F To Go to Frontpage'))
            print('-'*60)
            print("{:^60}".format('CARS'))
            print('-'*60)
            print('Press 1 to Show Available Cars')
            print('Press 2 to Show Unavailable Cars')
            print('Press 3 to Show Price List')
            print('Press 4 to Add A New Car To The Car Rental')
            print('Press F to Go To Frontpage')
            print()

        def main():
            print_Choices()
            action = ""  # so the while loop will start running
            while action not in ["1", "2", "3", "4", "F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*60)
                    print('Available Cars: \n')
                    self.__CarService.available_cars()
                    print()
                    print()

                elif action == '2':
                    print("-"*60)
                    print('Unavailable Cars: \n')
                    self.__CarService.unavailable_cars()
                    print()
                    print()

                elif action == '3':
                    print("-"*60)
                    print()
                    self.__CarService.show_Pricelist()
                    print()
                    print()

                elif action == '4':
                    print("-"*60)
                    print("New Car:")
                    licence_Plate = input('Enter The Licence Plate: ').upper()
                    category = self.__CarService.get_Category()
                    manufacturer = input('Enter The Manufacturer: ')
                    the_Type = input('Enter The Type: ')
                    transmission = self.__CarService.get_Transmission()
                    price = self.__CarService.get_Price()
                    new_Car = Car(licence_Plate, category, manufacturer, the_Type, transmission, price)
                    self.__CarService.add_car(new_Car)
                    print()
                    print('Car Added!\n\n')

                elif action == 'f':
                    break

                else:
                    print("Invalid input, try again!")

        main()

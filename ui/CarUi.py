from services.CarService import CarService
from models.Car import Car


class Car_Page:
    def __init__(self):
        self.__CarService = CarService()

    def car_Menu(self):

        def print_Choices():
            print('{:<30}{:>20}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Show Available Cars')
            print('Press 2 to Show Unavailable Cars')
            print('Press 3 to Show Price List')
            print('Press 4 to Add A New Car To The Car Rental')
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
                self.__CarService.show_Pricelist()

            elif action_Car == '4':
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

from services.CarService import CarService
from models.Car import Car

class Car_Page:
    def __init__(self):
        self.__CarService = CarService()

    def car_Menu(self):
        def print_Choices():
            ''' Prints out everything you can do with cars in the system '''
            print('{:<30}{:>20}'.format('The Car Rental', 'F To Go to Frontpage'))
            print('-'*50)
            print("{:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Show Available Cars')
            print('Press 2 to Show Unavailable Cars')
            print('Press 3 to Show Price List')
            print('Press 4 to Add A New Car To The Car Rental')
            print('Press F to Go To Frontpage')
            print()

        def main():
            print_Choices()
            print()
            action = ""  #so the while loop will start running
            while action not in ["1","2","3","4","F"]:
                action = input('Choose command: ').lower()
                if action == '1':
                    print("-"*15)
                    print('Available Cars: \n')
                    self.__CarService.available_cars()
                    print()
                
                elif action == '2':
                    print("-"*15)
                    print('Unavailable Cars: \n')
                    self.__CarService.unavailable_cars()
                    print()

                elif action == '3':
                    print("-"*15)
                    self.__CarService.show_Pricelist()
                    print()

                elif action == '4':
                    print("-"*15)
                    print("New customer:")
                    licence_Plate = input('Enter The Licence Plate: ').upper()
                    category = input('Enter The Category (Mini Car, Passenger Car, or Jeep): ').lower()
                    # category = ''
                    # while category != 'm' or 's' or 'j':
                    #     category = input('Enter The Category (M = Mini Car, S = Station Car, J = Jeep): ').lower()
                    #     if category == 'm':
                    #         category = 'Mini Car'
                    #     elif category == 's':
                    #         category = 'Station Car'
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
                    # try:
                    #     price = int(price)
                    # except ValueError:
                    #     print('Error! Please Enter Digits')
                    #     print()
                    #     þurfum að gera eh lykkju hér svo þetta runni þangað til það komi rétt input
                    #     price = input('Enter Price: ')
                    new_Car = Car(licence_Plate, category, manufacturer, the_Type, transmission, price)
                    self.__CarService.add_car(new_Car)
                    print()
                    print('Car Added!')
                    print()

                elif action == 'f':
                    break

                else:
                    print("Invalid input, try again!")

        main()

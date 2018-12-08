from services.CarService import CarService
from models.Car import Car
# from ui.FrontpageUi import Front_Page


class Car_Page:
    def __init__(self):
        self.__CarService = CarService()

    def car_Menu(self):

        def print_Choices():
            ''' Prints out everything you can do with cars in the system '''
            print('{:<30}{:>20}'.format('The Car Rental', 'B to go back'))
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
            if action == '1':
                print("-"*15)
                print('Available Cars: \n')
                print()
                self.__CarService.available_cars()
            
            elif action == '2':
                print("-"*15)
                print('Unavailable Cars: \n')
                print()
                self.__CarService.taken_cars()

            elif action == '3':
                print("-"*15)
                self.__CarService.show_Pricelist()

            elif action == '4':
                print("-"*15)
                print("New customer:")
                licence_Plate = input('Enter The Licence Plate: ').upper()
                category = input('Enter The Category (Mini Car, Passenger Car, or Jeep): ').lower()
                category = ''
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
                #     price = input('Enter Price: ')
                new_Car = Car(licence_Plate, category, manufacturer, the_Type, transmission, price)
                self.__CarService.add_car(new_Car)

<<<<<<< HEAD
            elif action == 'f':
                # ui = Front_Page()
                # ui.main_Menu()
                pass
=======
                elif action == 'f':
                    pass
                    # ui = Front_Page()
                    # ui.main_Menu()
                    
>>>>>>> 609b47672b5b6ed98dbbdd8eb836f4cee1c635f3

            else:
                print("Invalid input, try again!")

        main()

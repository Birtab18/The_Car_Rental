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
            print('{0:40}{1}'.format('Bílaleigan', 'B to go back'))
            print('-'*50)
            print("{0:>26}".format('Cars'))
            print('-'*50)
            print('Press 1 to Mark Car As Available For Rent')
            print('Press 2 to Mark Car As Not Available For Rent')
            print('Press 3 to Put In An Order')
            print('Press 4 to Cancel Order')
            print('Press 5 to Look Up Order')
            print('Press 6 to Change Order')
            print('Press 7 to Show Cars Availability')  # True or False
            print('Press 8 to Show Price List')
            print('Press 9 to Add A New Car To The Car Rental') 
            print('Press 10 to Change The Price List')
            print('Press q to Quit')
        
        # def sign_Up():

        def main():
            print_Choices() 
            action_Car = input('Choose command: ').lower()
            if action_Car == '1':
                print("mark car")
                pass
            elif action_Car == '2':
                pass
            elif action_Car == '3':
                print("-"*15)
                new_Or_Old = input('Has the customer rented a car from us before? y = Yes, n = No').lower()
                while new_Or_Old != 'y' or 'n':
                    if new_Or_Old == 'y':
                        #go to look up customer
                        pass
                    elif new_Or_Old == 'n':
                        #go to sign up new customer
                        pass
                    else:
                        print('Invalid input, try again!')

                print("New Order:")
                manufacturer = input('Enter The Manufacturer: ')
                the_Type = input('Enter The Type: ')
                transmission = input('Stick Shift Or Manual?: ')
                licence_Plate = input('Enter The Licence Plate: ')
                price = input('Enter Price: ')
                new_Car = Car(manufacturer, the_Type, transmission, licence_Plate, price)
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
                pass
            elif action_Car == '9':
                print("-"*15)
                print("New customer:")
                manufacturer = input('Enter The Manufacturer: ')
                the_Type = input('Enter The Type: ')
                transmission = input('Stick Shift Or Manual?: ')
                licence_Plate = input('Enter The Licence Plate: ')
                price = input('Enter Price: ')
                new_Car = Car(manufacturer, the_Type, transmission, licence_Plate, price)
                self.__CarService.add_car(new_Car)
            elif action_Car == '10':
                pass
            elif action_Car == 'q':
                pass
            else:
                print("Invalid input, try again!")

        main()
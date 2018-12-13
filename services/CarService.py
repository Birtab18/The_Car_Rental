from repo.CarOptions import CarOptions


class CarService:
    def __init__(self):
        # __checking_repo er private repository
        self.__car_Repo = CarOptions()

    def available_cars(self):
        self.__car_Repo.show_available_cars()

    def unavailable_cars(self):
        self.__car_Repo.show_unavailable_cars()

    def add_car(self, car):
        self.__car_Repo.add_car(car)  

    def show_Pricelist(self):
        self.__car_Repo.show_Pricelist()

    def check_Category(self, category):
        loop = True
        while loop:
            if category == 'm':
                category = 'Mini Car'
                loop = False
            elif category == 's':
                category = 'Station Car'
                loop = False
            elif category == 'j':
                category = 'Jeep'
                loop = False
            else:
                print("Invalid Input, Try Again!")
                category = input('Enter The Category (M = Mini Car, S = Station Car, J = Jeep): ').lower()
        return category

    def check_Transmission(self, transmission):
        loop = True
        while loop:
            if transmission == 's':
                transmission = 'Stick Shift'
                loop = False
            elif transmission == 'm':
                transmission = 'Manual'
                loop = False
            else:
                print('Invalid Input, Try Again!')
                transmission = input('Enter The Transmission (S = Stick Shift, M = Manual): ').lower()
        return transmission

    def check_Price(self, price):
        loop = True
        while loop:
            try:
                price = int(price)
                price = str(price)
                loop = False
            except ValueError:
                print('Invalid Input, Try Again! (only digits)')
                price = input('Enter Price: ')
        return price

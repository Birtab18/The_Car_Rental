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
        if self.is_valid_car(car):  # eru innputin sett in rett
            self.__car_Repo.add_car(car)  # ATH hvort repo eda main

    def is_valid_car(self, car):
        # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna.
        return True
        
    def show_Pricelist(self):
        self.__car_Repo.show_Pricelist()

    def get_Category(self):
        category = ""
        while category != 'm' or 's' or 'j':
            category = input('Enter The Category (M = Mini Car, S = Station Car, J = Jeep): ').lower()
            if category == 'm':
                category = 'Mini Car'
            elif category == 's':
                category = 'Station Car'
            elif category == 'j':
                category = 'Jeep'
            else:
                print("Invalid input, try again!")
        return category

    
from repo.CarOptions import CarOptions


class CarService:
    def __init__(self):
        # __checking_repo er private repository
        self.__car_Repo = CarOptions()

    def add_car(self, car):
        if self.is_valid_car(car):  # eru innputin sett in rett
            self.__car_Repo.add_car(car)  # ATH hvort repo eda main

    def is_valid_car(self, car):
        # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna.
        return True

    # def get_car(self):
    #     return self.__car_Repo.get_car()  # ATH hvort repo eda main

    # def delete_car(self):
    #     return self.__car_main.delete_car()
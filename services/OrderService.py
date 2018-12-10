from repo.OrderOptions import OrderOptions


class OrderService:
    def __init__(self):
        # __checking_repo er private repository
        self.__order_Repo = OrderOptions()

    def add_order(self, order):
        if self.is_valid_order(order):  # eru innputin sett in rett
            self.__order_Repo.add_order(order)  # ATH hvort repo eda main

    def is_valid_order(self, order):
        # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna.
        return True

    def look_up_order(self, SSN, licence_Plate):
        return self.__order_Repo.look_Up_Order(SSN, licence_Plate) # ATH hvort repo eda main

    def cancel_Order(self, SSN, licence_Plate):
        return self.__order_Repo.cancel_Order(SSN, licence_Plate)
    
    #def print_available_cars(self):
        #return self.__order_Repo.print_available_cars()
    
    def put_in_an_order(self,look_up,car_id,car_rent_year,car_rent_month,car_rent_day,car_return_year,car_return_month,car_return_day,total_price):
        self.__order_Repo.put_in_an_order(look_up,car_id,car_rent_year,car_rent_month,car_rent_day,car_return_year,car_return_month,car_return_day,total_price)

    def change_Order(self, SSN, choice, changes):
        self.__order_Repo.change_Order(SSN, choice, changes)

from repo.OrderOptions import OrderOptions


class OrderService:
    def __init__(self):
        # __checking_repo er private repository
        self.__order_Repo = OrderOptions()

    def add_order(self, customer):
        if self.is_valid_order(order):  # eru innputin sett in rett
            self.__order_Repo.add_order(order)  # ATH hvort repo eda main

    def is_valid_order(self, order):
        # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna.
        return True

    def get_order(self):
        return self.__order_Repo.get_order()  # ATH hvort repo eda main

    def cancel_Order(self, SSN, licence_Plate):
        return self.__order_Repo.cancel_Order(SSN, licence_Plate)
    
    def put_in_an_order(self,look_up,car_id,a,b,c,e,f,g):
        self.__order_Repo.put_in_an_order(look_up,car_id,a,b,c,e,f,g)

    def change_Order(self, ssn_number, choice, changes):
        self.__order_Repo.change_Order(ssn_number, choice, changes)

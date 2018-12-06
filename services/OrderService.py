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

    def delete_order(self):
        return self.__order_main.delete_order()
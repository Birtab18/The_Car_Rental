from repo.OrderOptions import OrderOptions


class OrderService:
    def __init__(self):
        # __checking_repo er private repository
        self.__order_Repo = OrderOptions()

    def look_up_order(self, SSN):
        return self.__order_Repo.look_Up_Order(SSN)

    def cancel_Order(self, SSN):
        return self.__order_Repo.cancel_Order(SSN)

    def put_in_an_order(self, SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day, car_return_year,
                        car_return_month, car_return_day, extra_insurance):
        self.__order_Repo.put_in_an_order(SSN, licence_Plate, car_rent_year, car_rent_month, car_rent_day, car_return_year,
                                          car_return_month, car_return_day, extra_insurance)

    def change_Order(self, SSN, choice, changes):
        self.__order_Repo.change_Order(SSN, choice, changes)

    def pick_a_category(self, car_choice):
        self.__order_Repo.pick_a_category(car_choice)

    def print_orders(self):
        self.__order_Repo.print_orders()

    def return_car(self, plate):
        self.__order_Repo.return_car(plate)

    def check_Car(self, licence_Plate):
        return self.__order_Repo.check_Car(licence_Plate)

    def check_Order(self, SSN):
        return self.__order_Repo.check_Order(SSN)

    def put_in_future_order(self, SSN, Name, Category, car_rent_year, car_rent_month, car_rent_day, car_return_year, car_return_month, car_return_day, extra_insurance):
        return self.__order_Repo.put_in_future_order(SSN, Name, Category, car_rent_year, car_rent_month, car_rent_day, car_return_year, car_return_month,
                                                     car_return_day, extra_insurance)

    def print_out_future_orders(self):
        return self.__order_Repo.print_out_future_orders()

    def remove_from_future_orders(self, SSN_input):
        return self.__order_Repo.remove_from_future_orders(SSN_input)

    def check_year(self, rent_year):
        loop = True
        while loop:
            if rent_year in ["2018", "2019"]:
                loop = False
            else:
                print('Invalid year')
                rent_year = input("Enter rent year: ")

        return rent_year

    def check_month(self, rent_month):
        loop = True
        while loop:
            if rent_month in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                loop = False
            else:
                print('Invalid month')
                rent_month = input("Enter rent month: ")

        return rent_month

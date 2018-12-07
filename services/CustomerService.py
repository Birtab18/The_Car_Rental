from repo.CustomerOptions import CustomerOptions


class CustomerService:
    def __init__(self):
        # __checking_repo er private repository
        self.__customer_Repo = CustomerOptions()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):  # eru innputin sett in rett
            self.__customer_Repo.add_customer(customer)  # ATH hvort repo eda main

    def is_valid_customer(self, customer):
        # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna.
        return True

    def look_up_customer(self, look_up):
        return self.__customer_Repo.look_up_customer(look_up)  # ATH hvort repo eda main

    def delete_customer(self, person_SSM):
        return self.__customer_Repo.delete_customer(person_SSM)

    def change_Customer_Info(self, person_Change, the_Change, new_Info):
        return self.__customer_Repo.change_Customer_Info(person_Change, the_Change, new_Info)

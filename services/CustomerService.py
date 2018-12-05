from repo.CustomerRepo import CustomerOptions

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerOptions() #__checking_repo er private repository

    def add_customer(self, customer):
        if self.is_valid_customer(customer): #eru innputin sett in rett
            self.__customer_main.add_customer(customer)

    def is_valid_customer(self, customer):
        #herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna. 
        return True

    def get_customer(self):
        return self.__customer_main.get_customer()











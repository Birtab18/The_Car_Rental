from repo.moguleikar import Customeroptions

class Checking2:
<<<<<<< HEAD:checking/doublechecking.py
    def __init__(self): # her fyrir ne
        self.__customer_main= Customeroption() #__checking_repo er private repository
=======
    def __init__(self):
        self.__customer_repo = Customeroptions() #__checking_repo er private repository
>>>>>>> 0e0aa4b3a234e9ef04b566c740cc466ee2092bc7:services/doublechecking.py

    def add_customer(self, customer):
        if self.is_valid_customer(customer): #eru innputin sett in rett
            self.__customer_main.add_customer(customer)

    def is_valid_customer(self, customer):
        #herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
        # ef valid þa addum vid þvi i gagnageymsluna. 
        return True

    def get_customer(self):
<<<<<<< HEAD:checking/doublechecking.py
        return self.__customer_main.get_customer()
=======
        pass
        #return self.__customer_repo.get_customer()
>>>>>>> 0e0aa4b3a234e9ef04b566c740cc466ee2092bc7:services/doublechecking.py











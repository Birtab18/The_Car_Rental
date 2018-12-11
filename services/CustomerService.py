from repo.CustomerOptions import CustomerOptions

class CustomerService:
    def __init__(self):
        # __checking_repo er private repository
        self.__customer_Repo = CustomerOptions()

    def add_customer(self, customer):
        self.__customer_Repo.add_customer(customer)

    # def is_valid_customer(self, customer):
    #     # herna rékkum vi hvort þetta video se ekki orugglega hægt af vinna med.
    #     # ef valid þa addum vid þvi i gagnageymsluna.
    #     return True

    def look_up_customer(self, SSN):
        return self.__customer_Repo.look_up_customer(SSN)  # ATH hvort repo eda main

    def delete_customer(self, SSN):
        return self.__customer_Repo.delete_customer(SSN)

    def Change_Information(self, SSN, choice, changes):
        self.__customer_Repo.Change_Information(SSN, choice, changes)
    
    def check_SSN(self, SSN):
        while len(SSN) != 10:
            print('Error! Please Input A Valid SSN (only 10 digits)\n')
            SSN = input('Enter The SSN: ')

        loop = True
        while loop:
            try:
                SSN = int(SSN)
                loop = False
            except ValueError:
                print('Error! Please Enter A Valid SSN (only 10 digits)\n')
                SSN = input('Enter The SSN: ')
        return SSN
    

    def check_Phonenumber(self, phonenumber):
        while len(phonenumber) != 7:
            print('Error! Please Input A Valid Phone Number (only 7 digits)\n')
            phonenumber = input('Enter A Phone Number: ')
        
        loop = True
        while loop:
            try:
                phonenumber = int(phonenumber)
                loop = False
            except ValueError:
                print('Error! Please Enter A Valid Phone Number (only 7 digits)\n')
                phonenumber = input('Enter A Phone Number: ')
        return phonenumber
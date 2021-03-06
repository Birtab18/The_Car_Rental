from repo.CustomerOptions import CustomerOptions

class CustomerService:
    def __init__(self):
        # __checking_repo er private repository
        self.__customer_Repo = CustomerOptions()

    def add_customer(self, customer):
        self.__customer_Repo.add_customer(customer)

    def look_up_customer(self, SSN):
        return self.__customer_Repo.look_up_customer(SSN)  

    def delete_customer(self, SSN):
        return self.__customer_Repo.delete_customer(SSN)

    def Change_Information(self, SSN, choice, changes):
        self.__customer_Repo.Change_Information(SSN, choice, changes)

    def check_SSN(self, SSN_input):
        while len(SSN_input) != 10:
            print('Invalid Input, Try Again! (only 10 digits)\n')
            SSN_input = input('Enter The SSN: ')
        loop = True
        while loop:
            try:
                SSN_input = int(SSN_input)
                SSN_input = str(SSN_input)
                loop = False
            except ValueError:
                print('Invalid Input, Try Again! (only 10 digits)\n')
                SSN_input = input('Enter The SSN: ')
        return SSN_input

    def check_Phonenumber(self, phonenumber_input):
        while len(phonenumber_input) != 7:
            print('Invalid Input, Try Again! (only 7 digits)\n')
            phonenumber_input = input('Enter A Phone Number: ')
        loop = True
        while loop:
            try:
                phonenumber_input = int(phonenumber_input)
                phonenumber_input = str(phonenumber_input)
                loop = False
            except ValueError:
                print('Invalid Input, Try Again! (only 7 digits)\n')
                phonenumber_input = input('Enter A Phone Number: ')
        return phonenumber_input

    def check_Choice(self, choice_input):
        while choice_input not in ['1', '2', '3', '4']:
            print('Invalid Input, Try Again!\n')
            choice_input = input('Enter Choice: ')
        return choice_input

    def check_Costumer(self,SSN_input):
        return self.__customer_Repo.check_Costumer(SSN_input)
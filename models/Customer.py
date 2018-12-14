'''This class is to get all of the informations we need about the customer'''
class Customer:

    def __init__(self, name, SSN, phonenumber, email):
        self.__name = name
        self.__SSN = SSN
        self.__phonenumber = phonenumber
        self.__email = email

    def __str__(self):
        return '{},{},{},{}'.format(self.__name, self.__SSN, self.__phonenumber, self.__email)
 
    def get_name(self):
        return self.__name
    
    def get_SSN(self):
        return self.__SSN

    def get_phonenumber(self):
        return self.__phonenumber

    def get_email(self):
        return self.__email
    



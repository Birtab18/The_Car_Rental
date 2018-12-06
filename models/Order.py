class Order:

    def __init__(self, rent_date, socialnumber, phonenumber, email):
        self.__name = name
        self.__socialnumber = socialnumber
        self.__phonenumber = phonenumber
        self.__email = email

    def __str__(self):
        return '{},{},{},{}'.format(self.__name, self.__socialnumber, self.__phonenumber, self.__email)
 
    def get_name(self):
        return self.__name
    
    def get_socialnumber(self):
        return self.__socialnumber

    def get_phonenumber(self):
        return self.__phonenumber

    def get_email(self):
        return self.__email
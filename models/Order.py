class Order:

    def __init__(self, SSN, Name, licence_plate, category, manufacturer, the_Type, rent_Date, return_date, extra_Insurance):
        self.__SSN = SSN
        self.__Name = Name
        self.__licence_plate = licence_plate
        self.__category = category
        self.__manufacturer = manufacturer
        self.__the_Type = the_Type
        self.__rent_Date = rent_Date
        self.__extra_Insurance = extra_Insurance
    
    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.__SSN, self.__Name, self.__licence_plate, self.__category, 
                            self.__manufacturer, self.__the_Type, self.__rent_Date, self.__extra_Insurance)

    def get_SSN(self):
        return self.__SSN
    
    def get_Name(self):
        return self.__Name

    def get_licence_plate(self):
        return self.__licence_plate

    def get_category(self):
        return self.__category
    
    def get_manufacturer(self):
        return self.__manufacturer
    def get_the_Type(self):
        return self.__the_Type

    def rent_Date(self):
        return self.__rent_Date

    def extra_Insurance(self):
        return self.__extra_Insurance

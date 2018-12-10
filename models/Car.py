class Car:

    def __init__(self, licence_Plate, category, manufacturer, the_Type, transmission, price, status=True):
        self.__licence_Plate = licence_Plate
        self.__category = category
        self.__manufacturer = manufacturer
        self.__the_Type = the_Type
        self.__transmission = transmission
        self.__price = price
        self.__status = status #True = available for rent

    def __str__(self):
        return '{},{},{},{},{},{},{}'.format(self.__licence_Plate, self.__category, self.__manufacturer, 
                self.__the_Type, self.__transmission, self.__price, self.__status)

    def get_licence_Plate(self):
        return self.__licence_Plate
    
    def get_category(self):
        return self.__category
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_the_Type(self):
        return self.__the_Type

    def get_transmission(self):
        return self.__transmission

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

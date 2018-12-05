class Car:

    def __init__(self, manufacturer, the_Type, transmission, color, price, status=True):
        self.__manufacturer = manufacturer
        self.__the_Type = the_Type
        self.__transmission = transmission
        self.__color = color
        self.__price = price
        self.__status = status #True = available for rent

    def __str__(self):
        return '{},{},{},{},{},{}'.format(self.__manufacturer, self.__the_Type, self.__transmission, 
                self.__color, self.__price, self.__status)
 
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_the_Type(self):
        return self.__the_Type

    def get_transmission(self):
        return self.__transmission

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status
    
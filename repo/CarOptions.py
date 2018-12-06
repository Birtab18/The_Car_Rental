from models.Car import Car

class CarOptions:

    def __init__(self):
        self.__car = []

    def add_car(self, car):
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/cars.csv', 'a+') as car_file:
            licence_Plate = car.get_licence_Plate()
            manufacturer = car.get_manufacturer()
            the_Type = car.get_the_Type()
            transmission = car.get_transmission()
            price = car.get_price()
            status = car.get_status()
            car_file.write('{},{},{},{},{},{}\n'.format(licence_Plate, manufacturer, the_Type, transmission,
                        price, status))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

 #breyta i car her f neðan

    # def get_customer(self):
    #     if self.__customer == []:  # first time this function is used
    #         with open('./data/customers.txt', 'r') as customer_file:
    #             for line in customer_file.readlines():
    #                 name, socialnumber, phonenumber, email = line.split(",")
    #                 new_costumer = Customer(name, socialnumber, phonenumber, email)
    #                 self.__customer.append(new_costumer)
    #         return self.__customer
    #     else:
    #         return self.__customer

    # def delete_customer(self):
    #     with open('./data/customers.txt', 'a+') as customer_file:
    #         customer_Delete = input("Enter Customers SSN number: ")
    #         for line in customer_file.readlines():
    #             if line != customer_Delete:
    #                 customer_file.write(line)
    #     return self.__customer

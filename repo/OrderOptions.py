from models.Order import Order
class OrderOptions:

    def __init__(self):
        self.__order = []

    def add_order(self, order):
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/orders.csv', 'a+') as order_file:
            name = customer.get_name()
            socialnumber = customer.get_socialnumber()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            customer_file.write('{},{},{},{}'.format(
                name, socialnumber, phonenumber, email))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

    def get_order(self):
        if self.__customer == []:  # first time this function is used
            with open('./data/order.csv', 'r') as order_file:
                for line in order_file.readlines():
                    name, socialnumber, phonenumber, email = line.split(",")
                    new_costumer = Customer(name, socialnumber, phonenumber, email)
                    self.__customer.append(new_costumer)
            return self.__customer
        else:
            return self.__customer

    def delete_customer(self):
        with open('./data/customers.csv', 'a+') as customer_file:
            customer_Delete = input("Enter Customers SSN number: ")
            for line in customer_file.readlines():
                if line not in customer_Delete:
                    customer_file.write(line)
        return self.__customer

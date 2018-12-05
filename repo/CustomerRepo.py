from models.Customer import Customer 

class CustomerOptions:

    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        #first add to file then to private list
        try:
            with open('./data/customers.csv', 'a+') as customer_file: #a+ = creates file if it doesnt exist
                name = customer.get_name()
                socialnumber = customer.socialnumber()
                phonenumber = customer.get_phonenumber()
                email = customer.get_email()
                customer_file.write('{},{},{},{}'.format(self.__name, self.__socialnumber, self.__phonenumber, self.__email))
        except:
            #adda þessu í skránna??? 1:18:20 i fyrirlestri 2
            pass

    def get_customer(self):
        if self.__customer == []: #first time this function is used
            with open('./data/customers.csv','r') as customer_file:
                for line in customer_file.readlines():
                    name, socialnumber, phonenumber, email = line.split(",")
                    new_costumer = Customer(name, socialnumber, phonenumber, email)
                    self.__customer.append(new_costumer)
                return self.__customer
        else:
            return self.__customer

 
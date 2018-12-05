from services.vidskiptavinir import Customer 

class Customeroptions:
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open('./data/customers.csv', 'a+') as customer_file: #a+ stendur fyrir ad skra verdur buin til ef thetta er ekki til
            name = customer.get_name()
            socialnumber = customer.get_socialnumber()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            customer_file.write('{},{},{},{}'.format(name, socialnumber, phonenumber, email))
            

    # def delete_costumer(self, customer):
    #     with open('./data/customers.csv','r') as customer_file:
            
    def get_customer(self):
        customer =[]
        with open('./data/customers.csv','r') as customer_file:
            for line in customer_file.readlines():
                name, socialnumber, phonenumber, email = line.split(",")
                new_costumer = Customer(name, socialnumber, phonenumber, email)
                customer.append(new_costumer)
            return customer

        
    # def delete_customer(self):
    #     with open('./data/customers.csv', 'a+') as customer_file:
    #         for row in customer_file:
    #             if row[1] == socialnumtodelete


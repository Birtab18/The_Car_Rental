from models.Customer import Customer 

class CustomerOptions:

    def __init__(self):
        self.__customer = []

    def add_Customer(self, customer):
        with open('./data/customers.txt', 'a+') as customer_file: #a+ stendur fyrir ad skra verdur buin til ef thetta er ekki til
            name = customer.get_length()
            socialnumber = customer.get_socialnumber()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            customer_file.write('{},{},{},{}'.format(name, socialnumber, phonenumber, email))

    def get_videos(self):
        customer =[]
        with open('./data/customers.txt','r') as customer_file:
            for line in customer_file.readlines():
                name, socialnumber, phonenumber, email = line.split(",")
                new_costumer = Customer(name, socialnumber, phonenumber, email)
                customer.append(new_costumer)
            return customer

    
    def delete_Customer:
        with open('./data/customers.txt','r') as customer_file:



 
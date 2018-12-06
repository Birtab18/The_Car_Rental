from models.Customer import Customer
import csv
class CustomerOptions:

    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/newcustomers.csv', 'a+') as customer_file:
            name = customer.get_name()
            socialnumber = customer.get_socialnumber()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            customer_file.write('{},{},{},{}'.format(
                name, socialnumber, phonenumber, email))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

    def get_customer(self):
        if self.__customer == []:  # first time this function is used
            with open('./data/newcustomers.csv', 'r') as customer_file:
                for line in customer_file.readlines():
                    socialnumber, name, phonenumber, email = line.split(",")
                    new_costumer = Customer(socialnumber, name, phonenumber, email)
                    self.__customer.append(new_costumer)
            return self.__customer
        else:
            return self.__customer

    def delete_customer(self):
        with open('./data/customers.csv', 'r') as inp, open('./data/newcustomers.csv', 'w') as out:
            writer = csv.DictWriter(out,fieldnames = ['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            person_delete = input('Enter the ssn of the person you want to delete: ')
            for row in csv.DictReader(inp):
                if row['SSN']!= person_delete:
                    writer.writerow(row)



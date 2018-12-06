from models.Customer import Customer
<<<<<<< HEAD
import os
=======
>>>>>>> bbe46cdd0351bf60e4858f09d02255b9dd990226
import csv
class CustomerOptions:

    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/customers.csv', 'a+') as customer_file:
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
        with open("./data/customers.csv", 'r') as f:
            reader = csv.reader(f)
            person_change = input('Enter the ssn of the person you want to look up: ')
            for row in reader:
                if row[0] == person_change:
                    print('SSN: {}\nName: {}\nTelephone: {}\nEmail: {}'.format(row[0],row[1],row[2],row[3]))



    def delete_customer(self):
        with open('./data/customers.csv', 'r') as inp, open('./data/newcustomers.csv', 'w') as out:
            writer = csv.DictWriter(out,fieldnames = ['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            person_delete = input('Enter the ssn of the person you want to delete: ')
            for row in csv.DictReader(inp):
                if row['SSN']!= person_delete:
                    writer.writerow(row)



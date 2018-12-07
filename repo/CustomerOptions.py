from models.Customer import Customer
import os
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
            customer_file.write('{},{},{},{}'.format(name, socialnumber, phonenumber, email))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

    def look_up_customer(self,look_up):
        with open("./data/customers.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[0] == look_up:
                    print('SSN: {}\nName: {}\nTelephone: {}\nEmail: {}'.format(row[0],row[1],row[2],row[3]))
                else:
                    print('Customer not found')

    def delete_customer(self, person_SSN):
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(out,fieldnames = ['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN']!= person_SSN:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/deletecustomers.csv', './data/customers.csv')
    
    def Change_Information(self):
        print('press 1 to change SSN')
        print('Press 2 to change Name')
        print('Press 3 to change Phone Number')
        print('Press 4 to change Email')
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            ssn_number = input('Enter the SSN of the person you want to change: ')
            writer = csv.DictWriter(out, fieldnames=['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i,value in row.items():
                    if value == ssn_number:
                        num = input('Enter num: ')
                        changes = input('Enter changed info: ')
                        choice = ''
                        if num == '1':
                            choice ='SSN'
                        elif num == '2':
                            choice = 'Name'
                        elif num == '3':
                            choice = 'Telephone_Number'
                        elif num == '4':
                            choice = 'Email'
                        row[choice] = changes
                        print(row)
                writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/deletecustomers.csv', './data/customers.csv')

# Til að eyða gömlu skránni og gera nýju skránna samnefnda gömlu skránni  






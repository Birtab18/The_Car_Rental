from models.Customer import Customer
import os
import csv
import os

class CustomerOptions:
    
    def __init__(self):
        self.__customer = []

    # Press 1 to Sign Up New Customer
    def add_customer(self, customer):
        ''' Adds a new customer to The Car Rental (the customers.csv file) '''
        # first add to file then to private list
        # try:
        # a+ = creates file if it doesnt exist
        with open('./data/customers.csv', 'a+') as customer_file:
            name = customer.get_name()
            SSN = customer.get_SSN()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            customer_file.write('\n{},{},{},{}'.format(name, SSN, phonenumber, email))
        # except:
            # adda þessu í skránna??? 1:18:20 i fyrirlestri 2
        # pass

    # Press 2 to Delete Customer 
    def delete_customer(self, person_SSN):
        ''' Deletes a customer from The Car Rental (from customers.csv file) '''
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN'] != person_SSN:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/deletecustomers.csv', './data/customers.csv')

    # Press 3 to Look Up Customer    
    def look_up_customer(self, SSN):
        ''' Looks Up a customer from The Car Rental (from customers.csv file) '''
        with open("./data/customers.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[0] == SSN:
                    #match.append('found')
                    print('SSN:{:10}{:<40}\nName:{:9}{:<40}\nTelephone:{:4}{:<40}\nEmail:{:8}{:<40}'.format
                            (" ", row[0], " ", row[1], " ", row[2], " ", row[3]))
            # if match == []:
            #     print('Customer Not Found')
                print()
            
    
    # Press 4 to Change Information About A Customer
    def Change_Information(self, SSN, choice, changes):
        ''' Changes information about a customer from The Car Rental (from customers.csv file) '''
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                for i,value in row.items():
                    if value == SSN:
                        the_Choice = ''
                        if choice == '1':
                            the_Choice ='SSN'
                            # if len(the_Choice) == 10:
                            #     row[the_Choice] = changes
                        elif choice == '2':
                            the_Choice = 'Name'
                        elif choice == '3':
                            the_Choice = 'Telephone_Number'
                        elif choice == '4':
                            the_Choice = 'Email'
                        row[the_Choice] = changes
                        print(row)
                writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/deletecustomers.csv', './data/customers.csv')
# Til að eyða gömlu skránni og gera nýju skránna samnefnda gömlu skránni  
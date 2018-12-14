from models.Customer import Customer
import os
import csv
import os

class CustomerOptions:
    def __init__(self):
        self.__customer = []

    #Check if the costumer exists
    def check_Costumer(self, SSN_input):
        with open("./data/customers.csv", 'r') as check_Costumer:
            reader = csv.reader(check_Costumer)
            for row in reader:
                # If the SSN matches one of the inputs it will return true
                if row[0] ==  SSN_input:
                    return True
                
    # Press 1 to Sign Up New Customer
    def add_customer(self, customer):
        ''' Adds a new customer to The Car Rental (the customers.csv file) '''
        with open('./data/customers.csv', 'a+') as customer_file:  # a+ = creates file if it doesnt exist
            # this is  collecting all of the informations about the customer: Name, SSN, Phonenumber, Email
            name = customer.get_name()
            SSN = customer.get_SSN()
            phonenumber = customer.get_phonenumber()
            email = customer.get_email()
            # Those informations are then used and written into "customers.csv"
            customer_file.write('{},{},{},{}\n'.format(name, SSN, phonenumber, email))

    # Press 2 to Delete Customer 
    def delete_customer(self, person_SSN):
        ''' Deletes a customer from The Car Rental (from customers.csv file) '''
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()   
            # It iterates through every row in the file, to try to find a match
            for row in csv.DictReader(inp):
                if row['SSN'] != person_SSN:
                    # For every line that is not a match, it will write that to a new file called deletecustomers
                    writer.writerow(row)
        #This deletes the old file, with the old informations
        os.remove('./data/customers.csv') 
        # This renames "deletecustomers" to "customers", like the old one with all of the old information exept for the one that was deleted
        os.rename('./data/deletecustomers.csv', './data/customers.csv') 


    # Press 3 to Look Up Customer   
    def look_up_customer(self, SSN):
        ''' Looks Up a customer from The Car Rental (from customers.csv file) '''
        with open("./data/customers.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            # It iterates through every row in the file, to try to find a match
            for row in reader:
                if row[0] == SSN:
                    # If the input matches index [0] it will print all the informations about the costumer
                    print('SSN:{:10}{:<40}\nName:{:9}{:<40}\nTelephone:{:4}{:<40}\nEmail:{:8}{:<40}'.format
                         (" ", row[0], " ", row[1], " ", row[2], " ", row[3]))

            
    
    # Press 4 to Change Information About A Customer
    def Change_Information(self, SSN, choice, changes):
        ''' Changes information about a customer from The Car Rental (from customers.csv file) '''
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(out, fieldnames=['SSN','Name','Telephone_Number','Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                # User choses a command, and depending on the command it will change that information
                for i,value in row.items():
                    if value == SSN:
                        the_Choice = ''
                        if choice == '1':
                            the_Choice ='SSN'
                        elif choice == '2':
                            the_Choice = 'Name'
                        elif choice == '3':
                            the_Choice = 'Telephone_Number'
                        elif choice == '4':
                            the_Choice = 'Email'
                        row[the_Choice] = changes
                writer.writerow(row)
        #This deletes the old file, with the old informations
        os.remove('./data/customers.csv') 
        # This renames "deletecustomers" to "customers", like the old one with all of the old information but with the changes. 
        os.rename('./data/deletecustomers.csv', './data/customers.csv')



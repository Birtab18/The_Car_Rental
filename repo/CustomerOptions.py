from models.Customer import Customer
import os
import csv
import os


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

    def look_up_customer(self, look_up):
        with open("./data/customers.csv", 'r') as look_up_customer_file:
            reader = csv.reader(look_up_customer_file)
            for row in reader:
                if row[0] == look_up:
                    print('SSN: {}\nName: {}\nTelephone: {}\nEmail: {}'.format(
                        row[0], row[1], row[2], row[3]))
                else:
                    print('Customer not found')

    def delete_customer(self, person_SSN):
        with open('./data/customers.csv', 'r') as inp, open('./data/deletecustomers.csv', 'w') as out:
            writer = csv.DictWriter(
                out, fieldnames=['Name', 'SSN', 'Telephone_Number', 'Email'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['SSN'] != person_SSN:
                    writer.writerow(row)
        os.remove('./data/customers.csv')
        os.rename('./data/deletecustomers.csv', './data/customers.csv')



    def change_Customer_Info(self, person_Change, the_Change, new_Info):
        customer_File = "./data/customers.csv"
        temp_File = NamedTemporaryFile(delete=False)

        with open(customer_File, 'r') as csv_File: #rb for binary
            reader = csv.DictReader(csv_File)
            writer = csv.DictWriter(temp_File, fieldnames=['SSN', 'Name', 'Phone Number', 'Email'])
            writer.writeheader()

            for row in reader:
                writer.writerow({"SSN": row["SSN"], "Name": row["Name"], "Phone Number": row["Phone Number"], 
                                "Email": row["Email"]}) #dictionary value
                if the_Change == '1':
                    row["SSN"] = new_Info
                    writer.writerow(row)
                elif the_Change == '2':
                    row["Name"] = new_Info
                    writer.writerow(row)
                elif the_Change == '3':
                    row["Phone Number"] = new_Info
                    writer.writerow(row)
                elif the_Change == '4':
                    row["Email"] = new_Info
                    writer.writerow(row)
                else: 
                    print("Invalid input, try again!")
        
        os.remove('./data/customers.csv')
        os.rename('./data/temp_File.csv', './data/customers.csv')  
            
            #shutil.move(temp_File, customer_File)


    # def change_Customer_Info(self):

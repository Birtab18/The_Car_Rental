from services.CustomerService import CustomerService
from models.Customer import Customer

class Frontpage:
    def __init__(self):
        self.__CustomerService = CustomerService()
        
    def main_menu(self):
        action = ''
        while (action !='q'):
            print('Press 1 for Customer')
            print('Press 2 for Car')
            print('Press q to Quit')
            action = input('Choose command: ').lower()

            if action =='1':
                print('Press 1 to Sign Up New Customer ')
                print('Press 2 to Delete Customer')
                print('Press 3 to Look Up Customer')
                print('Press 4 to Change Information About A Customer')
                print('Press q to Quit')
                action_Cust = input('Choose command: ').lower()

                if action_Cust == '1':
                    name = input('Enter a name: ')
                    socialnumber = input('Enter a SSN number: ')
                    phonenumber = input('Enter a phonenumber: ')
                    email = input('Enter an email: ')
                    new_costumer = Customer(name, socialnumber, phonenumber,email)
                    self.__CustomerService.add_customer(new_costumer)
                elif action_Cust == '2':
                    costumer = self.__CustomerService.get_costumer()
                elif action_Cust == '3':
                    pass
                elif action_Cust == '4':
                    pass
                elif action_Cust == 'q':
                    pass #quit
                else:
                    print("Invalid input, try again!") 


            elif action == '2':
                print('Press 1 to Mark Car As Available For Rent')
                print('Press 2 to Mark Car As Not Available For Rent')
                print('Press 3 to Put In An Order')
                print('Press 4 to Cancel Order')
                print('Press 5 to Look Up Order')
                print('Press 6 to Change Order')
                print('Press 7 to Show Cars Availability') #True or False
                print('Press 8 to Show Price List')
                print('Press q to Quit')
                action_Car = input('Choose command: ').lower()

                if action_Car == '1':
                    pass
                elif action_Car == '2':
                    pass
                elif action_Car == '3':
                    pass
                elif action_Car == '4':
                    pass
                elif action_Car == '5':
                    pass
                elif action_Car == '6':
                    pass
                elif action_Car == '7':
                    pass
                elif action_Car == '8':
                    pass
                elif action_Car == 'q':
                    pass #quit
                else:
                    print("Invalid input, try again!") 

            elif action == 'q':
                pass #quit
            
            else:
                print('Invalid input, try again!')
                


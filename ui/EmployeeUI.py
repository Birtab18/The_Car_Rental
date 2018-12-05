def front_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'Front page'))
    print('-'*50)
    print("{0:>26}".format('Hello'))
    print('-'*50)
    print("Press - 1 for Cars \nPress - 2 for Customers \nPress q to Quit ")


def car_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
    print('-'*50)
    print("{0:>26}".format('Cars'))
    print('-'*50)
    print("Press - 1 to Mark car as available for rent \nPress - 2 to Mark car as rented \nPress - 3 to Make Order \nPress - 4 to Cancel Order Press\nPress - 5 to Search for Order \nPress - 6 to Change Order\nPress - 7 for Car Status\nPress - 8 for Price list\nPress q to Quit ")


def customers_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
    print('-'*50)
    print("{0:>26}".format('Customers'))
    print('-'*50)
    print("Press - 1 for New Customer \nPress - 2 to Remove Customer  \nPress - 3 to Look up Customer\nPress - 4 to Edit Customer\nPress q to Quit ")


def main():

    choice = ''
    front_Page()
    while choice != 'q':
        choice = input('')
        if choice == '1':
            car_Page()
        elif choice == '2':
            customers_Page()
        elif choice == 'b':
            front_Page()
        elif choice == 'q':
            print('Goodbye!')
        else:
            print('Invalid option - Try again!')


main()

def front_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'Front page'))
    print('-'*50)
    print("{0:>26}".format('Hello'))
    print('-'*50)
    print("Press 1 for Cars \nPress 2 for Customers \nPress q to Quit")


def car_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
    print('-'*50)
    print("{0:>26}".format('Cars'))
    print('-'*50)
    print("Press 1 to Mark car as available for rent")
    print("Press 2 to Mark car as rented")
    print("Press 3 to Make Order")#hallo
    print("Press 4 to Cancel Order Press")
    print("Press 5 to Search for Order")
    print("Press 6 to Change Order")
    print("Press 7 for Car Status")
    print("Press 8 for Price list")
    print("Press q to Quit")


def customers_Page():
    print('{0:40}{1}'.format('Bílaleigan', 'B to back'))
    print('-'*50)
    print("{0:>26}".format('Customers'))
    print('-'*50)
    print("Press 1 for New Customer")
    print("Press 2 to Remove Customer")
    print("Press 3 to Look up Customer")
    print("Press 4 to Edit Customer")
    print("Press q to Quit")


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

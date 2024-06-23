from dest.action import add_dest, edit_dest, delete_dest
from dest.search import search, high_score
from storage.load_save import save, load


def menu():
    my_destinations = []
    load(my_destinations)
    while True: 
        print('1 - Add Destinations')
        print('2 - Edit Destinations')
        print('3 - Delete Destinations')
        print('4 - List Destinations')
        print('5 - Search Destinations')
        print('6 - Search Great Destinations')
        print('7 - Exit Program')
        selection = input('Select command')
        if selection == '1':
            add_dest(my_destinations)
        elif selection == '2':
            edit_dest(my_destinations)
        elif selection == '3':
            delete_dest(my_destinations)
        elif selection == '4':
            print(my_destinations)
        elif selection == '5':
            search(my_destinations)
        elif selection == '6':
            high_score(my_destinations)
        elif selection == '7':
            print('Program Terminated!!!')
            save(my_destinations)
            exit()

menu()

        
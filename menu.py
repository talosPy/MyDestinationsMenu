from dest.action import add_dest, edit_dest, delete_dest
from dest.search import search, high_score
from storage.load_save import save, load
from icecream import ic # to import ic from icecream package (inside venv!!!)
                        # !!!!! *ic* replaces the *print* using icecream !!!!!


def menu():
    my_destinations = []
    load(my_destinations)
    while True: 
        ic('1 - Add Destinations')
        ic('2 - Edit Destinations')
        ic('3 - Delete Destinations')
        ic('4 - List Destinations')
        ic('5 - Search Destinations')
        ic('6 - Search Great Destinations')
        ic('7 - Exit Program')
        selection = input('Select command')
        if selection == '1':
            add_dest(my_destinations)
        elif selection == '2':
            edit_dest(my_destinations)
        elif selection == '3':
            delete_dest(my_destinations)
        elif selection == '4':
            ic(my_destinations)
        elif selection == '5':
            search(my_destinations)
        elif selection == '6':
            high_score(my_destinations)
        elif selection == '7':
            ic('Program Terminated!!!')
            save(my_destinations)
            exit()

menu()

        
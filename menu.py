import json

FILE_NAME = 'destinations.json'

my_destinations = []



def add_dest():
    new_dest_name = input('Whats your Destination')
    new_dest_desc = input('Whats its Description')
    new_dest_score = input('Whats its Score')
    new_dest =  {'name' : new_dest_name,
                 'desc' : new_dest_desc,
                 'score': new_dest_score}
    my_destinations.append(new_dest)
    print("*Added Successfully*")


def delete_dest():
    del_dest_name = input('Choose the Destination you wish to remove')
    global my_destinations
    my_destinations = [destination for destination in my_destinations if destination['name'].lower() != del_dest_name.lower()]
    print(f"*The Destination: {del_dest_name} Has Been Deleted*")


def edit_dest():
    edit_dest_name = input('Edit your Destination name')
    found = False
    for destination in my_destinations:
        if destination['name'].lower() == edit_dest_name.lower():
            new_dest_name = input('Choose the new Destination :')
            new_dest_desc = input('Choose the Destination Description :')
            new_dest_score = input('Give the new Destination a Score')

            if new_dest_name:
                destination['name'] = new_dest_name
            if new_dest_desc:
                destination['desc'] = new_dest_desc
            if new_dest_score:
                destination['score'] = str(new_dest_score)

            print(f"Destination '{edit_dest_name}' has been Updated")
            found = True
            break
           

def search():
    print("*Search Started*")
    search_str = input("Please enter search str:")
    found = False
    for destination in my_destinations:
        if (
            search_str.lower() in destination['name'].lower()
            or search_str.lower() in destination['desc'].lower()
            or search_str.lower() in str(destination['score'])
        ):
            print(f"destination name: {destination["name"]}. desc: {destination["desc"]}. score: {destination["score"]}")
            found = True

    if not found:
        print('*INVALID DESTINATION*')
                

def high_score(min_score=8):
    print('*Searching Great Destinations*')
    found = False
    for destination in my_destinations:
        if int(destination['score']) >= min_score:
            print(f"Destination name: {destination['name']}. Desc: {destination['desc']}. Score: {destination['score']}")
            found = True

        if not found:
            print('*INVALID DESTINATION*')
    


def load():
    global my_destinations
    try:
        with open(FILE_NAME, 'r') as f:
            my_destinations = json.load(f)
    except:
        print("File Missing, Continuing...")
        my_destinations = []

                    
def save():
    with open(FILE_NAME, 'w') as f:   
        json.dump(my_destinations, f)


def menu():
    load()
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
            add_dest()
        elif selection == '2':
            edit_dest()
        elif selection == '3':
            delete_dest()
        elif selection == '4':
            print(my_destinations)
        elif selection == '5':
            search()
        elif selection == '6':
            high_score()
        elif selection == '7':
            print('Program Terminated!!!')
            save()
            exit()


menu()

        
def add_dest(my_destinations):
    new_dest_name = input('Whats your Destination')
    new_dest_desc = input('Whats its Description')
    new_dest_score = input('Whats its Score')
    new_dest =  {'name' : new_dest_name,
                 'desc' : new_dest_desc,
                 'score': new_dest_score}
    my_destinations.append(new_dest)
    print("*Added Successfully*")


# def delete_dest(my_destinations):
#     del_dest_name = input('Choose the Destination you wish to remove')
#     my_destinations = [destination for destination in my_destinations if destination['name'].lower() != del_dest_name.lower()]
#     print(f"*The Destination: {del_dest_name} Has Been Deleted*")

def delete_dest(my_destinations):
    del_dest_name = input('Choose the Destination you wish to remove: ')
    initial_length = len(my_destinations)
    my_destinations[:] = [destination for destination in my_destinations if destination['name'].lower() != del_dest_name.lower()]
    if len(my_destinations) < initial_length:
        print(f"*The Destination: {del_dest_name} Has Been Deleted*")
    else:
        print(f"*The Destination: {del_dest_name} Was Not Found*")



def edit_dest(my_destinations):
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
           

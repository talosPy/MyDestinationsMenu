def search(my_destinations):
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
                

def high_score(my_destinations, min_score=8):
    print('*Searching Great Destinations*')
    found = False
    for destination in my_destinations:
        if int(destination['score']) >= min_score:
            print(f"Destination name: {destination['name']}. Desc: {destination['desc']}. Score: {destination['score']}")
            found = True

        if not found:
            print('*INVALID DESTINATION*')
    

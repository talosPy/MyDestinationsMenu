import json

FILE_NAME = 'destinations.json'


# def load(my_destinations):                # STANDART JSON LOAD
#     try:
#         with open(FILE_NAME, 'r') as f:
#             my_destinations = json.load(f)
#     except:
#         print("File Missing, Continuing...")
#         my_destinations = []

                    
# def save(my_destinations):                # STANDART JSON SAVE
#     with open(FILE_NAME, 'w') as f:   
#         json.dump(my_destinations, f)


def load(my_destinations):
    try:
        with open(FILE_NAME, 'r') as f:
            destinations = json.load(f)
            my_destinations.extend(destinations)  # Append loaded destinations to the list
    except FileNotFoundError:
        print("File Missing, Continuing...")
    except json.JSONDecodeError:
        print("Error decoding JSON, continuing with empty list...")


def save(my_destinations):
    with open(FILE_NAME, 'w') as f:
        json.dump(my_destinations, f, indent=4)

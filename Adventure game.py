import time

# Define the rooms and their connections
rooms = {
    'room1': {'description': 'You are in a dark room with a door to the north.', 'north': 'room2'},
    'room2': {'description': 'You are in a hallway with doors to the north and south.', 'north': 'room3', 'south': 'room1'},
    'room3': {'description': 'You are in a brightly lit room with a door to the south.', 'south': 'room2'}
}

# Define the starting room
current_room = 'room1'

# Define the game loop
while True:
    # Print the current room's description
    print(rooms[current_room]['description'])
    
    # Ask the player for input
    command = input('What do you want to do? ')
    
    # Handle movement commands
    if command.lower() == 'north':
        if 'north' in rooms[current_room]:
            current_room = rooms[current_room]['north']
        else:
            print('You cannot go that way.')
    elif command.lower() == 'south':
        if 'south' in rooms[current_room]:
            current_room = rooms[current_room]['south']
        else:
            print('You cannot go that way.')
    elif command.lower() == 'quit':
        print('Thanks for playing!')
        break
    else:
        print('I do not understand that command.')
    
    # Add a delay for readability
    time.sleep(1)

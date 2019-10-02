from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room_map = {"Outside Cave Entrance":'outside', 'Foyer': 'foyer', 
            'Grand Overlook':'overlook', 'Narrow Passage':'narrow',
            'Treasure Chamber':'treasure'}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

items = {
  'torch': Item('torch', 'Use this to light your path into the cave!'),
  'sword': Item('sword', 'Use this to defend against any pirates you may encounter!'),
  'parachute': Item('parachute', 'Use this in case you slip and fall over the cliff, or if you are in the mood for basejumping!'),
  'moneybag': Item('moneybag', 'Use this to fill w/ gold and various treasure!'),
  'rum': Item('rum', 'Drink this aged bottle of rum to drown your sorrows!')
}

#add items to rooms:
room['outside'].items = [items['torch']]
room['foyer'].items = [items['sword']]
room['overlook'].items = [items['parachute']]
room['narrow'].items = [items['moneybag']]
room['treasure'].items = [items['rum']]
    
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player('outside')

user_input = ''
quit = False

while not quit:
  current_room = room[player.current_room] 
  print('\nYou are in the ' + current_room.name)
  print(current_room.description)
  print('Items available:')
  if len(current_room.items) == 0:
    print('\t **There are no items available in this room!**')
    user_input = input('Enter "n, s, e, w to go north, south, east, or west", or enter "q" to quit game:')
  else:
    for item in current_room.items:
      print(f'\t - {item}')
    user_input = input('To acquire an item, enter "get" or "take" followed by the item: Else, Enter "n, s, e, w to go north, south, east, or west", or enter "q" to quit game:').lower()
  if len(user_input) > 1:
    if user_input.split(' ')[0].lower() in ['get', 'take']:
      chosen_item = user_input.split(' ')[1].lower()
      room_item_names = [item.name for item in current_room.items]
      if chosen_item in room_item_names:
        item = items[chosen_item]
        item.on_take()
        player.items.append(item)
        current_room.items.remove(item)
      else:
        print('\t**Error, item entered not found, check spelling')
    elif user_input.split(' ')[0].lower() == 'drop':
      chosen_item = user_input.split(' ')[1].lower()
      player_item_names = [item.name for item in player.items]
      if chosen_item in player_item_names:
        item = items[chosen_item]
        item.on_drop()
        current_room.items.append(item)
        player.items.remove(item)
    elif user_input.lower() == 'inventory':
      print('\nCurrent inventory:')
      for item in player.items:
        print(f'\t - {item}')
    else:
      print('\t**Error, invalid input- unknown command')
  else:
    if user_input.lower() == 'n':
      try:
        player.current_room = room_map[room[player.current_room].n_to.name]
      except:
        print('\nError: "' + user_input + " direction not allowed.")
    elif user_input.lower() == 's':
      try:
        player.current_room = room_map[room[player.current_room].s_to.name]
      except:
        print('\nError: "' + user_input + " direction not allowed.")
    elif user_input.lower() == 'e':
      try:
        player.current_room = room_map[room[player.current_room].e_to.name]
      except:
        print('\nError: "' + user_input + " direction not allowed.")
    elif user_input.lower() == 'w':
      try:
        player.current_room = room_map[room[player.current_room].w_to.name]
      except:
        print('\nError: "' + user_input + " direction not allowed.")
    elif user_input.lower() == 'i':
      print('\nCurrent inventory:')
      for item in player.items:
        print(f'\t - {item}')
    elif user_input.lower() == 'q':
      quit = True
    else:
      print('\n**Error, unknown input')
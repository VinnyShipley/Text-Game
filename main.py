import time

# Global variables
inventory = {}
call_out_counter = 0

# FUNCTIONS

## SHOWING INVENTORY
def show_inventory():
  if len(inventory) == 0:
    print('There is nothing in your inventory')
  if len(inventory) >= 1:
    print('Current Inventory:')
    for item in inventory.values():
      print(item)



## WAKING UP
def first_response(initial_response):
  if initial_response == '1':
    initial_call_out()

  if initial_response == '2':
    initial_examine()
  
  if initial_response == '3':
    initial_sleep()
  
  if initial_response == '4':
    show_inventory()


## Calling out at first response
def initial_call_out():
  global call_out_counter
  if call_out_counter == 0:
    print(f'call out conter is this {call_out_counter}')
    call_out_counter += 1
    print('\'Hello? Is anybody there?\' You cry out.')
    time.sleep(1.8)
    print('''Nothing happens, no one responds. You appear to be alone.
Perhaps you should try something else''')
    post_callout_one()
  else:
    print(f'You call out again, to the same affect. Adventurous, aren\'t we?')
    post_callout_two()


def initial_examine():
  print('You see a glob on the nightstand. Do you reach out to take it and add it to your inventory? Y/N')
  add_glob = input('> ')

  string_glob = str(add_glob)

  if string_glob.lower() == 'y':
    inventory['glob'] = 'Glob'
    print('Glob added to inventory')
    show_inventory()

  if string_glob.lower() == 'n':
    print('That might be a good call, that looks like a particularly sticky glob')

def initial_sleep():
  print('this is where the sleep is going. Is this where you enter into the actual game? Every time that you sleep, something integral to the game changes')



## Still in bed after calling out once
def post_callout_one():
  print('''Let\'s try this again, shall we? As you are laying in the bed, what do you do?''')
  post_callout_response = input('''1. Call out
    2. Examine the room
    3. Go back to sleep
    4. Look into your inventory
    > ''')
  
  int_response = int(post_callout_response)
  
  if int_response == 1:
    initial_call_out()

  if int_response == 2:
    if len(inventory) == 0:
      initial_examine()
    if len(inventory) >= 1:
      print('The room seems bare now that you have taken that glob')
  
  if int_response == 3:
    initial_sleep()

  if int_response == 4:
    show_inventory()


## Still in bed after calling out twice
def post_callout_two():
  print('''You simply cannot call out again, that's not how this works. I\'m going to give you the option to, but you're gonna look like a real jagaloon if you call out again''')
  post_callout_response = input('''1. Call out
    2. Examine the room
    3. Go back to sleep
    4. Look into your inventory
    > ''')
  
  int_response = int(post_callout_response)
  
  if int_response == 1:
    print('Seriously? Well in that case, Goodbye')

  if int_response == 2:
    if len(inventory) == 0:
      initial_examine()
    if len(inventory) >= 1:
      print('The room seems bare now that you have taken that glob')
  
  if int_response == 3:
    initial_sleep()

  if int_response == 4:
    show_inventory()


# GAMEPLAY STARTS HERE
print('Welcome to the Game of Games')
game_username = input('Please enter your name: ')
print(f'''Well it turns out {game_username} imbibed in a little bit too much in something or other the night before. As a result they awaken in a strange room that they don\'t recognize. Do they:''')
initial_wake_up_prompt = input('''1. Call out
2. Examine the room
3. Go back to sleep
4. Look into your inventory
> ''')

first_response(initial_wake_up_prompt)




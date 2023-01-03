import time

# Global variables
inventory = {}
call_out_counter = 0

# FUNCTIONS

## SHOWING INVENTORY
def show_inventory():
  if len(inventory) == 0:
    print('There is nothing in your inventory')
  print('Inventory:')
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

def initial_call_out():
  call_out_counter =+ 1
  if call_out_counter > 0:
    print('the call out counter is working')
  print('\'Hello? Is anybody there?\' You cry out.')
  time.sleep(1.8)
  print('''Nothing happens, no one responds. You appear to be alone.
Looks like you're right back where you started''')

def initial_examine():
  print('You see a glob on the nightstand. Something compels you to take it')
  inventory['glob'] = 'Glob'
  show_inventory()
  

def initial_sleep():
  print('this is where the sleep is going. Is this where you enter into the actual game? Every time that you sleep, something integral to the game changes')


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



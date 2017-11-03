import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
user_choice = 0
items = ['paper', 'rock', 'scissors']
def user_choice_func(user_choice_text):
    global user_choice
    try:
        user_choice = items.index(user_choice_text)

        return user_choice
    except:
        print('No such element, try again')

def computer_choice_func():
    computer_choice = random.randint(0, 2)
    computer_choice_text = items[computer_choice]
    return computer_choice_text,computer_choice

def counting():
    global user_choice
    print('user:', user_choice)
    computer_choice = computer_choice_func()
    print('computer_choice:', computer_choice[0])
    if user_choice == computer_choice[1]:
        print('draw')
    elif user_choice + 1 == computer_choice[1] or (user_choice == 2 and computer_choice[1] == 0):
        print('user win')
    else:
        print('user lose')


f = simplegui.create_frame("Greeting",300,300)

f.add_input("Your choice", user_choice_func, 200)
f.add_button('Result', counting, 200)

f.start()

#counter = 0
#
#def print_counter():
#    global counter
#    print('This is', counter)
#
#def print_hello():
#    global counter
#    counter += 1
#    print_counter()
#
#def print_goodbye():
#    global counter
#    counter -= 1
#    print_counter()
#
#def zeroing():
#    global counter
#    counter = 0
#    print_counter()
#
#def inp(text):
#    global counter
#    counter = float(text)
#    print_counter()
#
#f = simplegui.create_frame("Greeting",300,300)
#
#f.add_button("+", print_hello, 200)
#f.add_button("-", print_goodbye, 200)
#f.add_button("0", zeroing, 200)
#f.add_input('Your counter', inp, 200)
#
#f.start()
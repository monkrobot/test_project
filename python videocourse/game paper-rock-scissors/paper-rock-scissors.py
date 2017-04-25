import random

items = ['paper', 'rock', 'scissors']
def user_choice_func():
    user_choice_text = input('Your choice: ')
    try:
        user_choice = items.index(user_choice_text)

        return user_choice
    except:
        print('No such element, try again')
        user_choice_func()

def computer_choice_func():
    computer_choice = random.randint(0, 2)
    computer_choice_text = items[computer_choice]
    return computer_choice_text,computer_choice

def counting(user_choice_func):
    user_choice = user_choice_func()
    print('user:', user_choice)
    computer_choice = computer_choice_func()
    print('computer_choice:', computer_choice[0])
    if user_choice == computer_choice[1]:
        print('draw')
    elif user_choice + 1 == computer_choice[1] or (user_choice == 2 and computer_choice[1] == 0):
        print('user win')
    else:
        print('user lose')

counting(user_choice_func)






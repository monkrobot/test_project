import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
#number = float('inf')
user_numb = -1


def number_generate():
    #global number
    number = random.randint(0,100)
    print(number)
    return number

number = number_generate()

def func123(user_number):
    global user_numb
    user_numb = user_number

def draw_number(canvas):
    global number
    canvas.draw_text("Welcome to the game", [10, 10], 20, 'White')
    canvas.draw_text("Guess The Number", [20, 40], 30, 'Red')
    if int(user_numb) < number:
        canvas.draw_text("Higher", [30, 90], 20, 'White')
    elif int(user_numb) > number:
        canvas.draw_text("Lower", [30, 90], 20, 'White')
    elif int(user_numb) == number:
        canvas.draw_text("You're right", [30, 90], 20, 'White')

f = simplegui.create_frame("Greeting",300,300)
f.add_button('Start', number_generate, 200)
f.add_input("Your choice", func123, 200)
f.set_draw_handler(draw_number)

f.start()

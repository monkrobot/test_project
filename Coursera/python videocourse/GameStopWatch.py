import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

special_timer = 0.000
player1 = 0
player2 = 0

def game_timer():
    global special_timer
    special_timer += 0.001

def button1_push(pos):
    global special_timer
    global player1
    if int(str(special_timer).split('.')[1]) >= 980 or int(str(special_timer).split('.')[1]) <= 20:
        player1 += 1
    else:
        player1 -= 1
    print('player1:', player1)

def button2_push(key):
    global special_timer
    global player2
    if int(str(special_timer).split('.')[1]) >= 980 or int(str(special_timer).split('.')[1]) <= 20:
        player2 += 1
    else:
        player2 -= 1
    print('player2:', player2)

def draw(canvas):
    global special_timer
    global player1, player2
    canvas.draw_text(str(special_timer), [50, 50], 30, 'White')
    canvas.draw_text(str(player1), [30, 20], 15, 'White')
    canvas.draw_text(str(player2), [70, 20], 15, 'White')

frame = simplegui.create_frame('Timer', 200, 200)

#frame.add_button("player1",button1_push, 100)
#frame.add_button('player2', button2_push, 100)
frame.set_mouseclick_handler(button1_push)
frame.set_keydown_handler(button2_push)
timer = simplegui.create_timer(1, game_timer)
frame.set_draw_handler(draw)

frame.start()
timer.start()
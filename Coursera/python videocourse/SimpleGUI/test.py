import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

flag = True
timer_time = 0

def timer_count():
    global timer_time
    timer_time += 0.001

def button_start():
    global flag
    flag = False
    global timer_time
    timer_time = 0

def button_finish():
    global flag
    flag = True
    global timer_time
    print(timer_time)


frame = simplegui.create_frame('Timer', 100, 100)

frame.add_button("start",button_start, 100)
frame.add_button('finish', button_finish, 100)
timer = simplegui.create_timer(1, timer_count)

frame.start()
timer.start()
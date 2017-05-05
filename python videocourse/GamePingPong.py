import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
asd = 0.2
platform_height = 50
platform_width = 10
platform_pos = 100

ball_pos = [WIDTH / 2, HEIGHT / 2]
#vel = [-40.0 / 60.0,  5.0 / 60.0]
vel = [-150.0 / 60.0,  150.0 / 60.0]

def keydown(key):
    global platform_pos, platform_height, HEIGHT, asd
    if key == simplegui.KEY_MAP['down'] and platform_pos+platform_height < HEIGHT:
        platform_pos += asd
    elif key == simplegui.KEY_MAP['up'] and platform_pos > 0:
        platform_pos -= 20


# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]


    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    #canvas.draw_polygon([(,),(,),(,),(,)])
    canvas.draw_polygon([[0, platform_pos], [platform_width, platform_pos], [platform_width, platform_height + platform_pos], [0, platform_height + platform_pos]], 12, 'Red')

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
# start frame
frame.start()
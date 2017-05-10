import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize globals
#Ball
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
#vel = [-40.0 / 60.0,  5.0 / 60.0]
vel = [-150.0 / 60.0,  150.0 / 60.0]
#Platform
asd = 0.2
platform_height = 50
platform_width = 10
platform_pos = 100
platform_pos2 = 100
#Players count
player1 = 0
player2 = 0

def keydown(key):
    global platform_pos, platform_pos2, platform_height, HEIGHT, asd
    # Changing of platform position with keys "Up" and "Down" for player1
    if key == simplegui.KEY_MAP['s'] and platform_pos+platform_height < HEIGHT:
        platform_pos += 20
    elif key == simplegui.KEY_MAP['w'] and platform_pos > 0:
        platform_pos -= 20

    # Changing of platform position with keys "Up" and "Down" for player2
    if key == simplegui.KEY_MAP['down'] and platform_pos2 + platform_height < HEIGHT:
        platform_pos2 += 20
    elif key == simplegui.KEY_MAP['up'] and platform_pos2 > 0:
        platform_pos2 -= 20

# define event handlers
def draw(canvas):
    global player1, player2
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # ball and walls collision
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
        player2 += 1
        print("Player 2:", player2)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
        player1 += 1
        print("Player 1:", player1)
    elif ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]
    #ball and platform1 collision
    elif ball_pos[0] - BALL_RADIUS == platform_width and platform_pos <= ball_pos[1] <= platform_pos + platform_height:
        vel[0] = - vel[0]
    # ball and platform2 collision
    elif ball_pos[0] + BALL_RADIUS == WIDTH - platform_width and platform_pos2 <= ball_pos[1] <= platform_pos2 + platform_height:
        vel[0] = - vel[0]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    #canvas.draw_polygon([(,),(,),(,),(,)])
    canvas.draw_polygon([[0, platform_pos], [platform_width, platform_pos],
                         [platform_width, platform_height + platform_pos], [0, platform_height + platform_pos]], 12, 'Red')
    canvas.draw_polygon([[WIDTH, platform_pos2], [WIDTH-platform_width, platform_pos2],
                         [WIDTH-platform_width, platform_height + platform_pos2], [WIDTH, platform_height + platform_pos2]], 12,
                        'Red')

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
# start frame
frame.start()
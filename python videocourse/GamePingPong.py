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
player1_up = 0
player1_down = 0
player2_up = 0
player2_down = 0

platform_height = 50
platform_width = 10
platform_pos = 100
platform_pos2 = 100
#Players count
player1 = 0
player2 = 0

def keydown(key):
    global platform_pos, platform_pos2, platform_height, HEIGHT, player1_up, player1_down, player2_up, player2_down
    # Changing of platform position with keys "Up" and "Down" for player1
    if key == simplegui.KEY_MAP['w']:
        player1_up = 10
    elif key == simplegui.KEY_MAP['s']:
        player1_down = 10

    # Changing of platform position with keys "Up" and "Down" for player2
    if key == simplegui.KEY_MAP['up']:
        player2_up = 10
    elif key == simplegui.KEY_MAP['down']:
        player2_down = 10

def keyup(key):
    global platform_pos, platform_pos2, player1_up, player1_down, player2_up, player2_down
    if key == simplegui.KEY_MAP['w']:
        player1_up = 0
    elif key == simplegui.KEY_MAP['s']:
        player1_down = 0

    # Changing of platform position with keys "Up" and "Down" for player2
    if key == simplegui.KEY_MAP['down']:
        player2_down = 0
    elif key == simplegui.KEY_MAP['up']:
        player2_up = 0

# define event handlers
def draw(canvas):
    global ball_pos, player1, player2, platform_pos, platform_pos2, player1_up, player1_down, player2_up, player2_down
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    if platform_pos + platform_height <= HEIGHT:
        platform_pos += player1_down
    if platform_pos >= 0:
        platform_pos -= player1_up

    if platform_pos2 + platform_height <= HEIGHT:
        platform_pos2 += player2_down
    if platform_pos2 >= 0:
        platform_pos2 -= player2_up


    # ball and walls collision
    if ball_pos[0] <= BALL_RADIUS:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel[0] = - vel[0]
        player2 += 1
        print("Player 2:", player2)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel[0] = - vel[0]
        player1 += 1
        print("Player 1:", player1)
    elif ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]
    #ball and platform1 collision
    elif ball_pos[0]-BALL_RADIUS <= platform_width and platform_pos-15 <= ball_pos[1] <= platform_pos + platform_height+15:
        vel[0] = - vel[0]
    # ball and platform2 collision
    elif ball_pos[0] + BALL_RADIUS == WIDTH - platform_width and platform_pos2-15 <= ball_pos[1] <= platform_pos2 + platform_height+15:
        vel[0] = - vel[0]

    # Draw ball
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([platform_width, 0], [platform_width, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - platform_width, 0], [WIDTH - platform_width, HEIGHT], 1, "White")
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
frame.set_keyup_handler(keyup)
# start frame
frame.start()
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

#cards values
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

counter = 0

#card
card_size = (72,96)
card_center = (36,48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

#card back side
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

class Random_card():
    def choise_card(self):
        global counter
        card_choice = (random.choice(RANKS), random.choice(SUITS))
        print(card_choice)
        print(counter)
        counter += 1
        return(card_choice)

class Dealler(Random_card):
    def dealler_card(self):
        card_choice = Random_card.choise_card(self)
        card_loc = (card_center[0] + card_size[0] * RANKS.index(card_choice[0]),
                    (card_center[1] + card_size[1] * SUITS.index(card_choice[1])))
        return(card_loc)

if counter < 1:
    card_draw = Dealler()
    card_loc = card_draw.dealler_card()
#draw function
def draw(canvas):
    # canvas.draw_image(picture, center of piece of picture to show, size of piece of picture to show
    #                              center of piece of canvas for picture, size of piece of canvas for picture)
    canvas.draw_image(card_images, card_loc, card_size, (300, 300), card_size)
    #card_loc = (card_center[0] + card_size[0]*RANKS.index(card_choice[0]),
    #            (card_center[1] + card_size[1]*SUITS.index(card_choice[1])))


#initial frame
frame = simplegui.create_frame("BlackJack", 600, 600)
frame.set_canvas_background("Green")

#buttons and canvas draw
frame.set_draw_handler(draw)

frame.start()
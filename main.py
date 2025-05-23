from pygame import *

back = (167,3,12)
win_width = 600
wih_height = 500
window = display.set_mode((win_width,wih_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update_r(self):

    def update_left(self):


game = True
finish = False
clock = time.Clock()
fps = 60

racket1 = Player('racket.png',30,200,4,50,150)
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSprite('tenis_ball.png', 200,200,4,50,150)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
from pygame import *
init()

W = 800
H = 500

window = display.set_mode((W, H))
bg = transform.scale(image.load('bg.jpeg'), (W, H))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = width
        self.height = height
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    keys_pressed = key.get_pressed()
    def update_l(self):
        if self.keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if self.keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y

    def update_r(self):
        pass


class Ball(GameSprite):
    pass

game = True
while game:
    window.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(100)
    display.update()
    





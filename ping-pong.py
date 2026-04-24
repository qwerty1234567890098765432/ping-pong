import pygame as pg
pg.init()

window = pg.display.set_mode((800, 500))
bg = (38, 123, 163)
window.fill(bg)
game = True

class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = randint(2, player_speed)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

FPS = 60
Clock = pg.time.Clock()
while game:
    for q in pg.event.get():
        if q.type == pg.QUIT:
            game = False
    pg.display.update()
    Clock.tick(FPS)

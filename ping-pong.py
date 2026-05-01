import pygame as pg
pg.init()

window = pg.display.set_mode((800, 500))
bg = (38, 123, 163)
window.fill(bg)
game = True

class GameSprite(pg.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Outline(self):
        pg.draw.rect(window, (255, 0, 0), self.rect, 5)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Update(GameSprite):
    def update_l(self):
        self.reset()
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pg.K_s] and self.rect.y < 360:
            self.rect.y += self.speed
    def update_r(self):
        self.reset()
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] and self.rect.y < 360:
            self.rect.y += self.speed

Ball = GameSprite('Ball.png', 200, 250, 5, 50, 50)
rocketL = Update('rocket.png', 10, 10, 5, 3, 130)
rocketR = Update('rocket.png', 785, 360, 5, 3, 130)

y_speed = 3
x_speed = 3

FPS = 60
Clock = pg.time.Clock()
while game:
    window.fill(bg)
    for q in pg.event.get():
        if q.type == pg.QUIT:
            game = False
    Ball.rect.x += x_speed
    Ball.rect.y -= y_speed
    if Ball.rect.y >= 455 or Ball.rect.y <= 0:
        y_speed *= -1
    if pg.sprite.collide_rect(Ball, rocketL):
        x_speed *= -1
    if pg.sprite.collide_rect(Ball, rocketR):
        x_speed *= -1
    rocketL.update_l()
    rocketR.update_r()
    rocketL.Outline()
    rocketR.Outline()
    Ball.reset()
    pg.display.update()
    Clock.tick(FPS)

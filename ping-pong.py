import pygame as pg
pg.init()
bounces_count = 0
window = pg.display.set_mode((800, 500))
bg = (38, 123, 163)
window.fill(bg)
game = True
font1 = pg.font.Font(None, 60)
finish = False

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

y_speed = 4
x_speed = 4
you_loseL = font1.render('LEFT LOSE!', True, (200, 0, 0))
you_loseR = font1.render('RIGHT LOSE!', True, (200, 0, 0))

FPS = 60
Clock = pg.time.Clock()
while game:
    for q in pg.event.get():
        if q.type == pg.QUIT:
            game = False
    if finish != True:
        window.fill(bg)
        Ball.rect.x += x_speed
        Ball.rect.y -= y_speed
        if Ball.rect.y >= 455 or Ball.rect.y <= 0:
            y_speed *= -1
        if pg.sprite.collide_rect(Ball, rocketL):
            x_speed *= -1
            bounces_count += 1
        if pg.sprite.collide_rect(Ball, rocketR):
            x_speed *= -1
            bounces_count += 1
        if bounces_count == 3:
            bounces_count = 0
            y_speed += 1
            x_speed += 1
        if Ball.rect.x <= 0:
            finish = True
            window.blit(you_loseL, (15, 225))
        if Ball.rect.x >= 750:
            finish = True
            window.blit(you_loseR, (515, 225))
        rocketL.update_l()
        rocketR.update_r()
        rocketL.Outline()
        rocketR.Outline()
        Ball.reset()
    pg.display.update()
    Clock.tick(FPS)

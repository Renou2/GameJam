import pygame as pg
vec = pg.math.Vector2
GRAVITE = 0.0


class Personnage(pg.sprite.Sprite):
    def __init__(self, image):
        self.speed = 1
        self.image = image
        self.rect = image.get_rect()
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    def jump(self, LISTE):
        self.rect.y += 1
        collide = pg.sprite.spritecollide(self, LISTE, False)
        self.rect.y-=1
        if collide:
            self.vel.y = -13
            if collide[0].type == 4:
                self.vel.y = -24

    def update(self, LISTE):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -0.5
        if keys[pg.K_RIGHT]:
            self.acc.x = 0.5
        # equations of motion
        self.acc.x += self.vel.x * -0.12
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

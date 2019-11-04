import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, ai_settings, screen, image, x, y, type_):
        super(Blocks, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image_ = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x = float(x)
        self.image_index = 1
        self.type_ = type_
        self.up = False
        self.down = False
        self.ypos = y
        self.up_g = 0
        self.down_g = 0
        self.dead = 0

    def image_up(self):
        self.image_index += 1

    def blitme(self):
        if self.type_ == "bricks" and self.dead == 1:
            self.kill()

        if self.up_g > 0:
            self.rect.y -= 2
            self.up_g -= 1
        if self.down_g > 0:
            self.rect.y += 2
            self.down_g -= 1
        if self.up_g == 0 and self.up is True:
            self.up = False
            self.down_g = 5

        if self.type_ != "hidden" and self.type_ != "invs" and self.type_ != "winner":
            self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.image_index == 1:
            self.image = self.image

    def blipup(self, music, mario):
        if self.up_g == 0 and self.down_g == 0 and self.type_ != "reg" and self.type_ != "v" \
                and self.type_ != "3bar" and self.type_ != "2bar" and self.type_ != "cbrick":
            self.up_g = 5
            self.up = True

            if self.type_ == "pup" or self.type_ == "star":
                self.type_ = "v"
                self.image = pygame.image.load("assets/interactible/qblock_used_1.bmp")
                pygame.mixer.Channel(2).play(music.pup_spawn)
            elif self.type_ == "pup2" or self.type_ == "pup3" or self.type_ == "star2":
                self.type_ = "v"
                self.image = pygame.image.load("assets/interactible/qblock_used_2.bmp")
                pygame.mixer.Channel(2).play(music.pup_spawn)

            elif self.type_ == "qcoin" or self.type_ == "bcoin":
                self.type_ = "v"
                self.image = pygame.image.load("assets/interactible/qblock_used_1.bmp")
                pygame.mixer.Channel(2).play(music.coin)

            elif self.type_ == "qcoin2" or self.type_ == "bcoin2":
                self.type_ = "v"
                self.image = pygame.image.load("assets/interactible/qblock_used_2.bmp")
                pygame.mixer.Channel(2).play(music.coin)

            elif self.type_ == "hidden" or self.type_ == "1up2" or self.type_ == "u":
                if self.image_ == 'assets/interactible/qblock_used_2.bmp':
                    pygame.mixer.Channel(2).play(music.coin)
                else:
                    pygame.mixer.Channel(2).play(music.pup_spawn)
                if self.type_ == "1up2":
                    self.image = pygame.image.load("assets/interactible/qblock_used_2.bmp")
                self.type_ = "v"

            else:
                if mario.state == "super" or mario.state == "fire":
                    pygame.mixer.Channel(2).play(music.bbreak)
                else:
                    pygame.mixer.Channel(2).play(music.bbump)

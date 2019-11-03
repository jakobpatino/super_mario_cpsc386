import pygame
from pygame.sprite import Group
from mario import Mario
from settings import Settings
from level_monitor import Monitor
from scores import Scoreboard
import functions as gf
from music import Music

mainClock = pygame.time.Clock()


def run_game():
    pygame.init()
    pygame.display.set_caption("Mario")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    scores = Scoreboard(ai_settings, screen)
    music = Music()

    g_blocks = Group()
    bg_blocks = Group()
    enemies = Group()
    chunks = Group()
    items = Group()

    pygame.mixer.set_reserved(0)
    pygame.mixer.set_reserved(1)
    pygame.mixer.set_reserved(2)
    pygame.mixer.set_reserved(3)
    pygame.mixer.set_reserved(4)
    pygame.mixer.set_reserved(5)

    monitor = Monitor(ai_settings, screen, g_blocks, bg_blocks, chunks, enemies, items)
    mario = Mario(ai_settings, screen, g_blocks, bg_blocks, enemies, monitor, chunks, items, scores)

    while True:
        gf.check_events(ai_settings, screen, mario, g_blocks, bg_blocks, items, music)
        mario.update(music, mario)
        gf.check_time(ai_settings, scores, mario)
        gf.check_lives(ai_settings, scores)
        music.check_star(mario)
        music.check_dies(mario)
        music.check_win(mario)
        music.change_bg_music()

        gf.update_screen(ai_settings, screen, mario, g_blocks, bg_blocks, enemies, monitor,
                         chunks, items, scores, music)

        mainClock.tick(40)


run_game()

import sys

import pygame

from settings import Settings
from bei_jing_tu import Bei_jing
from ship import Ship
import game_function as gf
def run_game():
    # chu shi hua you xi 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    bei_jing = Bei_jing(screen)

    #开始游戏主循环
    while True:

        #监视鼠标和键盘事件
        gf.update_screen(ai_settings,screen,bei_jing,ship)
        gf.check_events(ship)
        ship.update()


run_game()
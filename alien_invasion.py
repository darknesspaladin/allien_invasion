import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from bei_jing_tu import Bei_jing
from ship import Ship
from alien import Alien
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
    #创建一个用于存储子弹的编组、一个外星人编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #bei_jing = Bei_jing(screen)

    #开始游戏主循环
    while True:

        #监视鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets) 
        bullets.update() 
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
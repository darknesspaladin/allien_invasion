import sys

import pygame

def check_keydown_events(event,ship):
    """按键按下的相应"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """按键抬起的响应"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 右\左移
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        # 右移停止
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
     
def update_screen(ai_settings,screen,bei_jing,ship):

    #每次循环时重新汇屏以及背景飞船等内容
    screen.fill(ai_settings.bg_color)
    bei_jing.blitpic()
    ship.blitme()    

    #让绘制的屏幕刷新并可见
    pygame.display.flip()

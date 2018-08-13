import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """按键按下的相应"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """按键抬起的响应"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 右\左移
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        # 右移停止
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
     
def update_screen(ai_settings,screen,ship,alien,bullets):
    #每次循环时重新汇屏以及背景飞船等内容
    screen.fill(ai_settings.bg_color)
    #bei_jing.blitpic()
    #在飞船和外星人后面重绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.blitme()
    #让绘制的屏幕刷新并可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    #更新子弹位置
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没到达限制，就发射2颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人并能计算一行能够容纳多少个外星人
    #外星人间距为外星人的宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_apace_x = aisettings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x / (2 * alien_width)

    #创建第一行外星人并将其加入到当前列
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        
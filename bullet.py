import pygame
from pygame.sprite import Sprite

class Bullet(sprite):
    """一个对飞船发射子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        
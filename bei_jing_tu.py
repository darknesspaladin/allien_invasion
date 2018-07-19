import pygame

class  Bei_jing():

    def __init__(self,screen):
        self.screen = screen

        # 导入背景图案
        self.bei_jing_tu = pygame.image.load('images/bei_jing.bmp')

        # 或得背景图的外接矩形
        self.bjt_rect = self.bei_jing_tu.get_rect()
        self.screen_rect = screen.get_rect()

        self.bjt_rect.centerx = self.screen_rect.centerx
        self.bjt_rect.centery = self.screen_rect.centery

    def blitpic(self):
        """绘制背景图案"""
        self.screen.blit(self.bei_jing_tu,self.bjt_rect)

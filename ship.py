import pygame

class Ship():

    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 获取飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标识
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标识调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 2
        if self.moving_left:
            self.rect.centerx -= 2

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
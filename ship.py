import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 获取飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        #将每艘新飞船放置在屏幕底部中央
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # 移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标识调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        #更新rect对象
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
class Settings():
    """存储外星人中所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕相关设置
        self.screen_width = 900
        self.screen_height = 660
        self.bg_color = (255,255,255)
        self.ship_speed_factor = 2.5
        #子弹的设置
        self.bullet_speed_factor = 1.5
        self.bullet_color = (60,60,60)
        self.bullet_width = 3
        self.bullet_height = 15
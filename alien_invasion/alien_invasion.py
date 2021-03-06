import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game():
    #初始化
    pygame.init()
 
    # screen = pygame.display.set_mode((800,600))    #创建窗口
    # pygame.display.set_caption("Alien Invasion")
    # bg_color = (230,230,230)
    
    #使用类进行初始化
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # 游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     # 每次循环都重绘屏幕
        #     #screen.fill(bg_color)
        #     screen.fill(ai_settings.bg_color)
        #     ship.blitme()
        #     # 让最近绘制的屏幕可见
        #     pygame.display.flip()
run_game()
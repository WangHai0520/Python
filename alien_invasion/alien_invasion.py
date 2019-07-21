import sys
import pygame

def run_game():
    #初始化
    pygame.init()
    screen = pygame.display.set_mode((800,600))    #创建窗口
    pygame.display.set_caption("Alien Invasion")
    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #让最近绘制的屏幕可见
            pygame.display.flip()
run_game()
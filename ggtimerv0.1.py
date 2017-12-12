# 重写ggtimer
# 实现窗口

# 引入
import pygame
# 初始化
pygame.init()
size = width, height = 600, 400                                     # 初始窗口大小
screen = pygame.display.set_mode(size, pygame.RESIZABLE)            # 设置窗口大小和模式
icon = pygame.image.load('g.png')                                   # 图标
pygame.display.set_icon(icon)                                       # 设置图标
pygame.display.set_caption("GGtime")                                # 设置标题

# 响应
while 1:
    for event in pygame.event.get():                                # 响应事件
        if event.type == pygame.QUIT:                               # 退出事件
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:                      # 窗口大小调节
            size = width, height = event.size[0], event.size[1]     # 重新设置窗口大小
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# 刷新
    pygame.display.update()

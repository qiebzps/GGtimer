# 在屏幕上打印倒计时
'''
框架：
    引入
        函数
    初始化
    响应
        刷新
'''

# 引入
import pygame, sys

# 初始化
pygame.init()
size = width, height = 600, 400
icon = pygame.image.load("g.png")                               # 图标
count = 0
fps = 1
fclock = pygame.time.Clock()                                    # 
fontsize = 200                                                  # 字体大小
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)        # 窗口尺寸和模式
pygame.display.set_caption("GGtimer")                           # 标题
pygame.display.set_icon(icon)
timer = int(input("input time"))

# 响应
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if count < timer:
        last = str(timer-count)
        print(last)
        screen.fill(black)
        count += 1

    # 刷新
    fclock.tick(fps)

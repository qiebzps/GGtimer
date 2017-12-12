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
import pygame, sys, time

# 初始化
pygame.init()
size = width, height = 600, 400
icon = pygame.image.load("g.png")                               # 图标
count = 0
fps = 1
fclock = pygame.time.Clock()                                    # 
fontsize = 200                                                  # 字体大小
black = 0, 0, 0
write = 255,255,255
fontsize = 200
# pos = 10,10
pos = width/2, height/2
font = pygame.font.SysFont("宋体",fontsize)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)        # 窗口尺寸和模式
pygame.display.set_caption("GGtimer")                           # 标题
pygame.display.set_icon(icon)
timer = int(input("input time"))

def ggtimer(screen,count, timer, fontsize, pos):

    font = pygame.font.SysFont("宋体",fontsize)
    text = font.render(str(timer), 1, write)
    screen.blit(text, pos)
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    while (timer-count > 0):
        count += 1
        last = str(timer - count)
        text = font.render(last, 1, write)
        screen.blit(text, pos)
        pygame.display.update()
        screen.fill(black)
        pygame.time.Clock().tick(1)
    if count == timer:
        return 1
        
        
ggtimer(screen, count, timer, fontsize, pos)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

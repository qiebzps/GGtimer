# 文字放置在屏幕中心位置

import pygame

size = width, height =  600, 400
write = 255, 255, 255
screen = pygame.display.set_mode(size, pygame.RESIZABLE)         # 设置屏幕大小及模式
fontObj = pygame.font.SysFont("宋体", 200)                  # 创建一个font对象
textSurfaceObj = fontObj.render("hello world", 1, write)    # 创建一个存放文字的surface对象
textRectObj = textSurfaceObj.get_rect()                     # 文字图像位置
textRectObj.center = (width/2, height/2)

screen.blit(textSurfaceObj, textRectObj)

pygame.display.update()




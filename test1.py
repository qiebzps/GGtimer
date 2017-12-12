import pygame

pygame.init()

vInfo = pygame.display.Info()
# size = width, height = 1500, 400
write = 255, 255, 255

while 1:
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    fontObj = pygame.font.SysFont('宋体', 200)
    textSurfaceObj = fontObj.render("lskjfd", 1, write)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (width/2, height/2)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.display.update()




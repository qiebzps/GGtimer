import pygame

pygame.init()

size = width, height = 600, 400
write = 255, 255, 255
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            fontObj = pygame.font.SysFont("宋体", 200)
            textSurfaceObj = fontObj.render("lsdkjflsdjf", 1, write)
            pos = width/2, height/2
            textRect = textSurfaceObj.get_rect()
            textRect.center = pos
            screen.blit(textSurfaceObj, textRect)

        pygame.display.update()


import time, pygame

def numSleep(num):
    '''
    num 是int
    给我一个num，过一秒，我将返回(num-1)
    author:zps
    mail:1033239636@qq.com
    '''
    if num > 0:                                                                     # 时间大于0
        time.sleep(1)                                                               # 暂停1秒
        num -= 1                                                                    # num 自减1
    return num                                                                      # 返回num

def numToMS(num):
    '''
    num 是int
    给我一个num，我将它转化为分秒，并返回str(分：秒)
    author:zps
    main:1033239636@qq.com
    '''
    m = num//60                                                                     # 分
    s = num%60                                                                      # 秒
    if m < 10:                                                                      # 当分为9,8,7,...时，显示为09，08，07，...
        m = "0" + str(m)
    if s < 10:                                                                      # 当秒为9,8,7,...时，显示为09，08，07，...
        s = "0" + str(s)
    ret = str(m) + ':' + str(s)                                                     # ret为str
    return (ret)

def scrStr(screen, string):
    '''
    screen 是窗口名称
    string 是字符串
    在screen中心打印string
    author:zps
    mail:1033239636@qq.com
    '''
    fontsize = 200                                                                  # 字体大小
    write = 255,255,255                                                             # RGB颜色
    black = 0,0,0
    font = pygame.font.SysFont('宋体', fontsize)                                    # 字体
    text = font.render(string, 1, write)                                            # 内容
    textRec = text.get_rect()                                                       # 内容get_rect
    textRec.center = screen.get_rect().center                                       # 将屏幕中心设为打印内容的中心从而让内容居中
    screen.fill(black)                                                              # 填充
    screen.blit(text, textRec)                                                      # 将内容打印到屏幕中心
    pygame.display.update()                                                         # 刷新

def numIsZero(num):
    '''
    num 是int
    给我一个数字，如果它是1，那么我就播放音乐
    author:zps
    main:1033239636@qq.com
    '''
    if num == 1:
        pygame.mixer.music.load('g.wav')
        pygame.mixer.music.play(1)

pygame.init()

size = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GGtimer")
icon = pygame.image.load('g.png')
pygame.display.set_icon(icon)

timer = 5                                # 秒
num = timer

while 1:
    string = numToMS(num)
    scrStr(screen, string)
    num = numSleep(num)
    numIsZero(num)
    pygame.display.update()

'''


增加功能：
    无

未解决：
    计时误差(甲.time.sleep(1)使程序暂停1秒，乙.程序其余语句也将耗费时间    结果也就是（甲+乙>1）,使得长时间运行可导致显而易见的计时错误)

未实现:
    统计（生成统计文件）
    查看统计

author:zps
mail:1033239636@qq.com

'''
import time, pygame                                     # 引入time 和 pygame模块
import sys                                              # 引入sys模块

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
    mail:1033239636@qq.com
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
    # font = pygame.font.SysFont('宋体', fontsize)                                    # 字体
    font = pygame.font.Font('VeraMoBd.ttf', fontsize)                                    # 字体
    text = font.render(string, 1, write)                                            # 内容
    textRec = text.get_rect()                                                       # 内容get_rect
    textRec.center = screen.get_rect().center                                       # 将屏幕中心设为打印内容的中心从而让内容居中
    screen.fill(black)                                                              # 填充
    screen.blit(text, textRec)                                                      # 将内容打印到屏幕中心
    pygame.display.update()                                                         # 刷新

def numIsZero(num):
    '''
    num 是int
    return 0
    给我一个数字，如果它是0，那么我就播放音乐
    author:zps
    mail:1033239636@qq.com
    '''
    if num == 0:
        pygame.mixer.music.load('g.wav')
        pygame.mixer.music.play(1)
        return 0

def exitXEsc():
    '''
    响应退出
    author:zps
    mail:1033239636@qq.com
    '''
    for event in pygame.event.get():                    # 响应退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:              ## 响应esc退出
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

pygame.init()                                           # pygame初始化

size = 600, 400                                         # 窗口大小
screen = pygame.display.set_mode(size)                  # 窗口大小及模式设置
pygame.display.set_caption("GGtimer")                   # 标题
icon = pygame.image.load('g.png')                       # 图标
pygame.display.set_icon(icon)                           # 图标设置
fpsClock = pygame.time.Clock()

# main loop
while 1:
    # 屏幕初始化打印25:00
    scrStr(screen,"25:00")
    # timer = 5
    timer = 1500                                        # 25分钟 
    num = timer

    # 响应
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 响应按键
        elif event.type == pygame.KEYDOWN:
            # 响应空格
            if event.key == pygame.K_SPACE:
                while num != 0:
                    exitXEsc()                          # 使在计时中可退出
                    string = numToMS(num)               # 将num转化为分秒
                    scrStr(screen,string)               # 屏幕打印
                    num = numSleep(num)                 # num - 1
                    if numIsZero(num) == 0:
                        # 计时结束则打印00:00 
                        scrStr(screen,"00:00")
                        time.sleep(1)
                        # 屏幕初始化打印05:00
                        scrStr(screen,"00:00")
                        # timer = 3
                        timer = 300                     # 5分钟
                        num = timer
                        while num != 0:
                            exitXEsc()                  # 使在计时中可退出
                            string = numToMS(num)       # 将num转化为分秒
                            scrStr(screen,string)       # 屏幕打印
                            num = numSleep(num)         # num - 1
                            if numIsZero(num) == 0:
                                # 计时结束则打印00:00 
                                scrStr(screen,"00:00")
                                time.sleep(1)
                            print("O")
                    print("OK")

            # 响应<ESC>退出
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


'''
已解决bug:
    未引入sys模块
    字体宽度不一致导致的位置变动

增加功能：
    番茄钟的休息时间及结束提醒

未解决：
    计时误差(甲.time.sleep(1)使程序暂停1秒，乙.程序其余语句也将耗费时间    结果也就是（甲+乙>1）,使得长时间运行可导致显而易见的计时错误)

将来实现:
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
    给我一个数字，如果它是0，那么我就播放音乐
    author:zps
    mail:1033239636@qq.com
    '''
    if num == 0:
        pygame.mixer.music.load('g.wav')
        pygame.mixer.music.play(1)

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

def timer():
    '''
    倒计时
    author:zps
    mail:1033239636@qq.com
    '''
    # 25 分钟工作
    scrStr(screen,"25:00" )                             # 开始计时时在屏幕中心打印"25:00"

    for event in pygame.event.get():                    # 响应退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:              ## 响应esc退出
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_UP:              # UP键开始计时
                timer = 5                               ## 演示计时5秒
                #timer = 1500
                num = timer
                while 1:
                    exitXEsc()                          # 响应退出
                    string = numToMS(num)               # 将num 转化为 分：秒  
                    scrStr(screen, string)              # 将字符串打印到屏幕中心
                    num = numSleep(num)                 # 延时1秒
                    numIsZero(num)                      # 判断num是否为0,为0则播放音频
                    string = numToMS(num)               # 不是与上边的重复了，是为了解决当num为0时无法打印的问题
                    scrStr(screen, string)              # 不是与上边的重复了，是为了解决当num为0时无法打印的问题
                    pygame.display.update()             # 刷新屏幕
                    if num == 0:                        # num 为0 ,进入休息倒计时
                        # 5 分钟休息
                        time.sleep(1)
                        scrStr(screen,"05:00" )         # 开始计时时在屏幕中心打印"25:00"
                        time.sleep(1)

                        # timer = 3                     ## 演示计时3秒
                        timer = 300                     # 5分钟
                        num = timer
                        while 1:
                            exitXEsc()                  # 响应退出
                            string = numToMS(num)       # 将num 转化为 分：秒  
                            scrStr(screen, string)      # 将字符串打印到屏幕中心
                            num = numSleep(num)         # 延时1秒
                            numIsZero(num)              # 判断num是否为0,为0则播放音频
                            string = numToMS(num)       # 不是与上边的重复了，是为了解决当num为0时无法打印的问题
                            scrStr(screen, string)      # 不是与上边的重复了，是为了解决当num为0时无法打印的问题
                            pygame.display.update()     # 刷新屏幕
                            if num == 0:                # num 为0 时，跳出
                                break
                        break


pygame.init()                                           # pygame初始化

size = 600, 400                                         # 窗口大小
screen = pygame.display.set_mode(size)                  # 窗口大小及模式设置
pygame.display.set_caption("GGtimer")                   # 标题
icon = pygame.image.load('g.png')                       # 图标
pygame.display.set_icon(icon)                           # 图标设置


while 1:
    timer()

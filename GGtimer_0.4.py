#自行实现timer功能
#0.3将功能写成函数
#0.4将@ggtimer函数的输出优化为倒计时数
#import time
#count = 0
#timer =int( input('请输入倒计时时间，单位为秒:'))
#while (count < timer):
#    count += 1
#    time.sleep(1)
#    print(count)
#print('done')


import time
def ggtimer(count,timer):
    '''
    倒计时功能函数，
    '''
    while(count < timer):
        count += 1
        time.sleep(1)
        print(timer - count)
    print("done")
    return 1


timer = int(input("time:"))
count = 0
ggtimer(count,timer)

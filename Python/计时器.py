import time;import winsound
str=input('请输入计时时间（s）：')
t=int(str)
n=1
x=t
print('                                    '+repr(t)+'\n')
while n<=t-1:
    time.sleep(0.9)
    winsound.Beep(600,100)
    n=n+1
    print('                                    '+repr(x-1)+'\n')
    x=x-1
time.sleep(1)
print('                                  '+'时间到！')
winsound.Beep(800,500)

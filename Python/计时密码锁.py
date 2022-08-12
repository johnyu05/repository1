import time;import winsound
dic={1:'恭喜你获得奖章！',2:'密码错误，请再试一次\n',3:'次数已用尽，请10s后再试！\n'}
n=0
x=0
while n<=4:
    n=n+1
    str = input("请输入密码：");
    if str=='密码':
        print(dic[1])
        break
    else :
        if n!=5:
            print(dic[2])
        else :
            print(dic[3])
            while x<=4:
                x=x+1
                m=1
                y=10
                print('\n'+repr(10)+'\n')
                while m<=9:
                    time.sleep(0.9)
                    winsound.Beep(600,100)
                    m=m+1
                    print(repr(y-1)+'\n')
                    y=y-1
                time.sleep(1)
                print('0'+'\n')
                winsound.Beep(800,500)
                str = input("请输入密码：");
                if str=='密码':
                    print(dic[1])
                    break
                else :
                    if x==5:
                        time.sleep(1)
                        print('你的所有机会已用尽！')
                    elif x==4:
                        print('密码错误，你还有最后一次机会！')
                    else:
                        print('密码错误，请10s后再试！')
            

dic={1:'恭喜你获得奖章！',2:'请再试一次',3:'次数已用尽！'}
n=0
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

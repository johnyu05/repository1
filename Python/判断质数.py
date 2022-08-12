d=1
while d==1:
    str=input('数字：')
    n=int(str)
    for x in range(2,n):
        if   n % x ==0:
            print(n, ' 不是质数')
            break
    else :
        print(n,'是质数')

import math;import fractions;import time
str1,str2,str3=input('二次项系数：'),input('一次项系数：'),input('常数项：')
a,b,c=fractions.Fraction(str1),fractions.Fraction(str2),fractions.Fraction(str3)
d=b**2-4*a*c
if d<0 :
    print('\n'+'该方程无实数根')
elif d==0:
    x0=-b/(2*a)
    print('\n'+'该方程只有一个实数根，为：'+'\n'+'x='+str(x0))
else :
    e=math.sqrt(d)
    tuple=math.modf(e)
    if tuple[0]==0.0 :
        t=int(e)
        x1=(t-b)/(a*2)
        x2=(-t-b)/(a*2)
        print('\n'+'该方程有两个实数根，为：'+'\n'+'X1='+str(x1)+'\n'+'X2='+str(x2))
    else :
        t=d
        n=1
        h=1
        list=[1]
        while n<=100000:
            m=t/n**2
            tuple1=math.modf(m)
            if tuple1[0]==0.0:
                f=str(n)
                list[0]=f
            n=n+1
        h=fractions.Fraction(f)
        t=t/h**2
        k=a*2
        if k==1:
            print('\n'+'该方程有两个实数根，为：'+'\n'+'X1='+str(-b)+'+'+str(h)+'√'+str(t)+\
                    '\n'+'X2='+str(-b)+'-'+str(h)+'√'+str(t))
        elif k==-1:
            print('\n'+'该方程有两个实数根，为：'+'\n'+'X1='+str(b)+'+'+str(h)+'√'+str(t)+\
                    '\n'+'X2='+str(b)+'-'+str(h)+'√'+str(t))
        else :
            print('\n'+'该方程有两个实数根，为：'+'\n'+'X1='+'('+str(-b)+'+'+str(h)+'√'+str(t)+')'+'/'+str(k)+\
                    '\n'+'X2='+'('+str(-b)+'-'+str(h)+'√'+str(t)+')'+'/'+str(k))
time.sleep(2)


import turtle as t

#输入（x，y）的处理
b,d='',''
lin=list(input('(x,y):'+'\n'))
n=int(lin.index(','))
m=int(lin.index(')'))
for i in range(1,n):
    a=lin[i]
    b=b+a
    x=int(b)
for j in range(n+1,m):
    c=lin[j]
    d=d+c
    y=int(d)

#移动（x,y）
t.setup(500,500)
t.colormode(255)
t.pensize(20)

t.penup()
t.goto(-100+x,75+y)
t.pd()
t.goto(100+x,95+y)

t.pu()
t.goto(-50+x,-5+y)
t.pd()
t.goto(50+x,5+y)

t.pu()
t.goto(0+x,85+y)
t.pd()
t.goto(0+x,-85+y)

t.pu()
t.goto(-150+x,-100+y)
t.pd()
t.goto(150+x,-70+y)

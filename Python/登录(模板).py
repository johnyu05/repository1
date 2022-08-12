import time;import turtle as t
A=['2923692762','1']
AP={'2923692762':'yhj123abc','1':'1'}
At=input('Account:')
if At in A:
    for i in range(4):
        Pw = input("Password：");
        
        if Pw ==AP[At]:#Right Pw
            print('密码正确'+'\n'+'请3s后输入验证码')
            #王
            t.setup(500,500)
            t.colormode(255)
            t.pensize(20)

            t.penup()
            t.goto(-100,75)
            t.pd()
            t.goto(100,95)

            t.pu()
            t.goto(-50,-5)
            t.pd()
            t.goto(50,5)

            t.pu()
            t.goto(0,85)
            t.pd()
            t.goto(0,-85)

            t.pu()
            t.goto(-150,-100)
            t.pd()
            t.goto(150,-70)
            time.sleep(3)

            for i in range(3):
                Ck=input('您看到的汉字是：')
                if Ck in ['王','1']: #Right check
                    print('Welcome!')
                    '''以下可为登录后可执行内容
                        ......
                    '''
                    break
                else: #Wrong check
                    print('验证码错误')
            break

        else : #Wrong Pw
            if i==3:
                print('次数已用尽!')
            else :
                print('请再试一次')


                
else: #Wrong At
    print('账号不存在!')

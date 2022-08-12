import time;import turtle as t
A=['2923692762','1']
AP={'2923692762':'123abc','1':'1'}
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
            time.sleep(1)

            for i in range(3):
                Ck=input('您看到的汉字是：')
                if Ck in ['王','1']: #Right check
                    print('Welcome!'+'\n')
                    aa=0
                    while aa==0 :
                        choose=input('加密请输入K,翻译请输入T,其它任意键注销：'+'\n')
#加密
                        if choose in ['K','k']:
                            import random

                            dic_1={'a':31,'b':32,'c':11,'d':21,'e':41,'f':33,'g':34,\
                                 'j':22,'k':37,'l':23,'m':42,'n':38,'o':12,'p':24,\
                                 'q':25,'r':39,'s':13,'t':26,'u':14,'v':27,'w':43,\
                                 'x':28,'y':51,'z':52,'A':31,'B':32,'C':11,'D':21,\
                                 'E':41,'F':33,'G':34,'H':35,'I':36,'h':35,'i':36,\
                                 'J':22,'K':37,'L':23,'M':42,'N':38,'O':12,'P':24,\
                                 'Q':25,'R':39,'S':13,'T':26,'U':14,'V':27,'W':43,\
                                 'X':28,'Y':51,'Z':52,'7':'x','8':'y','9':'z'}

                            dic_2={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',\
                                   10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',\
                                   19:'s',20:'t',21:'u',22:'v',23:'w'}

                            #input
                            whole_para=[]
                            para=input('one para:'+'\n')

                            # !and?
                            list_input=list(para)
                            n_list_input=len(list_input)
                            para=''
                            for n in range(n_list_input):
                                if list_input[n] == '!':
                                    list_input[n]='.7'
                                    para+=list_input[n]
                                elif list_input[n] == '?':
                                    list_input[n]='.8'
                                    para+=list_input[n]
                                elif list_input[n] == '.':
                                    list_input[n]='.9'
                                    para+=list_input[n]
                                else :
                                    para+=list_input[n]

                            #sen
                            sen_list=para.split('.')
                            n_sen=len(sen_list)
                            if sen_list[n_sen-1]=='':
                                del sen_list[n_sen-1]
                                n_sen-=1

                            #senp
                            for i in range(n_sen):
                                whole_para+=[dic_2[random.randint(1,23)]]
                                senp_list=sen_list[i].split(',')
                                n_senp=len(senp_list)
                                                
                            #word
                                for j in range(n_senp):
                                    whole_para+=[dic_2[random.randint(1,23)]]
                                    word_list=senp_list[j].split(' ')
                                    n_word=len(word_list)
                            #letter
                                    for k in range(n_word):
                                        whole_para+=[dic_2[random.randint(1,23)]]
                                        letter_list=list(word_list[k])

                            #sum
                                        for l in letter_list:
                                            w=dic_1[l]
                                            whole_para+=[w]

                            #end
                            whole_para+=['/END']

                            #print
                            n_whole_para=len(whole_para)
                            print('START/',end='')
                            for n in range(n_whole_para):
                                print(whole_para[n],end='')
                            print('\n')
                             
#翻译
                        
                        elif choose in ['T','t']:
                            dic_1={31:'a',32:'b',11:'c',21:'d',41:'e',33:'f',34:'g',\
                                   35:'h',36:'i',22:'j',37:'k',23:'l',42:'m',38:'n',\
                                   12:'o',24:'p',25:'q',39:'r',13:'s',26:'t',14:'u',\
                                   27:'v',43:'w',28:'x',51:'y',52:'z'}
                            dic_2={31:'A',32:'B',\
                                   11:'C',21:'D',41:'E',33:'F',34:'G',35:'H',36:'I',\
                                   22:'J',37:'K',23:'L',42:'M',38:'N',12:'O',24:'P',\
                                   25:'Q',39:'R',13:'S',26:'T',14:'U',27:'V',43:'W',\
                                   28:'X',51:'Y',52:'Z'}
                            letter=['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i','j',\
                                    'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's','t',\
                                    'u', 'v','w', 'x', 'y', 'z']

                            #input
                            task_list_p=list(input('请输入：'+'\n'))
                            n_task_list_p=len(task_list_p)
                            task_list=task_list_p[9:n_task_list_p-4]
                            n_task_list=len(task_list)

                            list_letter=[];sen=[];senp=[];word=[]
                            #letter(for next
                            for i in range(0,n_task_list):
                                if task_list[i] in letter:
                                    list_letter+=[i]
                            n_list_letter=len(list_letter)

                            # (! / ? / .) / , / ' '
                            add=0
                            for i in range(0,n_list_letter-3):
                                i+=add
                                if i>n_list_letter-3:
                                    break
                                else:
                                    if list_letter[i+3]==list_letter[i]+3:
                                        sen+=[i]
                                        add+=3
                                    elif list_letter[i+1]==list_letter[i]+1:
                                        senp+=[i]
                                        add+=1
                                    else:
                                        word+=[i]
                                        add+=0
                            #each point
                            sen_pt=[]
                            for i in sen:
                                sen_pt+=[list_letter[i]]
                            senp_pt=[]
                            for i in senp:
                                senp_pt+=[list_letter[i]]
                            word_pt=[]
                            for i in word:
                                word_pt+=[list_letter[i]]

                            #print
                            pt=sen_pt+senp_pt+word_pt
                            add=0
                            for i in range(0,n_task_list,2):
                                i+=add
                                if i>=n_task_list:
                                    break
                                else:
                                    if i in sen_pt:
                                        add+=2
                                        if task_list[i+3]=='x':
                                            print('!',end='')
                                        elif task_list[i+3]=='y':
                                            print('?',end='')
                                        elif task_list[i+3]=='z':
                                            print('.',end='')
                                    elif i in senp_pt:
                                        add+=0
                                        print(',',end='')
                                    elif i in word_pt:
                                        add-=1
                                        print(' ',end='')
                                    else:
                                        print(dic_1[int(str(task_list[i])+str(task_list[i+1]))],end='')
                            print('\n')
                         
                        else:
                            aa=1
                            print('已注销!')
                        
                    break
                else: #Wrong check
                    print('验证码错误')
            break

        else : #Wrong Pw
            if i==3:
                print('次数已用尽!')
            else :
                print('请再试一次')
else:
    print('账号不存在!')
exit=input('\n'+'任意输入退出程序：'+'\n')

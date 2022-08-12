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

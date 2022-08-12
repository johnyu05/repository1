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



        





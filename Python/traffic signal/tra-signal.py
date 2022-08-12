'''This is a traffic-signaled system
Requirement:
    1.Cars and trucks need at least 40s(4s)' passing time.
    2.Pedestrians need 40s(4s)'
    3.cannot turn right when the right zebra is working.
    4.The different directions passing time need be satisfyied.
    5.Had better make a whole passing time least.
    6.direction:East,West,North,South
    7.Green:1  ; Red:0
    8*.Within this,cars can turn right freely
'''

#Start here
import time
START=time.time()
#stn=stw=ste=wte=wtn=wts=nts=nte=ntw=etw=ets=etn=0#Cars
#n=s=e=w=0#Pedestrians
Na{}
La=['stn','stw','ste','wte','wtn','wts','nts','nte','ntw','etw','ets','etn','n','s','e','w']
Da={'stn':0,'stw':0,'ste': 0,'wte':0,'wtn':0,'wts':0,'nts':0,'nte':0,'ntw':0,'etw':0,'ets':0,'etn':0,\
    'n':0,'s':0,'e':0,'w':0}
Ln=len(La)
Lp=[]#allow to pass
def check():
    global Da
    global Lp
    for i in La:
        if Da[i]==1:
            Lp+=[i]
    print(Da)
    time.sleep(4)
    for i in La:
        if Da[i]==1:
            Da[i]=0
    Lp=[]
    print('Done')
#above(cannot be review)
Da['e']=Da['stn']=Da['wtn']=1
check()
Da['n']=Da['etw']=Da['stw']=1
check()
Da['w']=Da['nts']=Da['etw']=1
check()
Da['s']=Da['wte']=Da['nte']=1
check()
print('one T is finished.')


#below(cannot be review)
END=time.time()
print('It took you:'+str(round(END-START,1))+'s')
#End here

u=float(input('来个体温：'))
T=5*(u-32)/9
print('Your tem is:'+'%0.2f'%T+'°C')
if T>=37.2:
    print('You have a fever!!!')
else:
    print('You are fine!')


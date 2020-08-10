ch=int(input('Enter the classes held on total: '))
ca=int(input('Enter the classes attended on total: '))
cap=(ca/ch)*100
a=str(input('If any medical issue y/n : '))
if(a=='y' or a=='Y' or a=='n' or a=='N'):
    print(cap,'% of class attended')
    if(cap<75 and (a=='n'or a=='N')):
        print('He/She not allowed to attend exam')
    else:
        print('He/She allowed to attend exam')
else:
    print('INVALID')

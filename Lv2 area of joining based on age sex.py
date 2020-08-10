a=int(input('Enter the age: '))
s=str(input('Enter the sex M/F: '))
m=str(input('Enter the martial Status Y/N: '))
if(a>20 and a<60):
    if(s=='f' or s=='F'):
        print('sholud work in urban areas only')
    elif(s=='m' or s=='M'):
        if(a>20 and a<40):
            print('can work anywhere')
        elif(a>=40 and a<60):
            print('Should work in urban areas only')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')

            

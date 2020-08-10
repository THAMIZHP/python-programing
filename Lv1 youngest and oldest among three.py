'''b=50
b1=50
b2=50
if(b==b1==b2):
    print('all are equal')
else:
    if(b1<=b and b2<=b):
        print(b,'is oldest')
    elif(b<=b1 and b2<=b1):
        print(b1,'is oldest')
    elif(b1<=b2 and b<=b2):
        print(b2,'is oldest')
    if(b1>=b and b2>=b):
        print(b,'is youngest')
    elif(b>=b1 and b2>=b1):
        print(b1,'is youngest')
    elif(b1>=b2 and b>=b2):
        print(b2,'is youngest')'''
#or this method
b=50
b1=50
b2=75
if(b==b1==b2):
    print('all are equal')
else:
    if(b1<=b and b2<=b):
        print(b,'is oldest')
        if(b1<=b2):
            print(b1,'is youngest')
        else:
            print(b2,'is youngest')
    elif(b<=b1 and b2<=b1):
        print(b1,'is oldest')
        if(b<=b2):
            print(b,'is youngest')
        else:
            print(b2,'is youngest')
    elif(b1<=b2 and b<=b2):
        print(b2,'is oldest')
        if(b1<=b):
            print(b1,'is youngest')
        else:
            print(b,'is youngest')


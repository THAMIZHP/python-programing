'''From a list containing ints, strings and floats, make three lists to
store them separately.'''

a=['thamizh', 3000, 'pavi', 3.00]
b,c,d=[],[],[]
for x in a:
    if (isinstance(x,int)):
        b.append(x)
    elif(isinstance(x,float)):
        c.append(x)
    elif(isinstance(x,str)):
        d.append(x)
    else:
        print('Type Invalid')
print('The int type items in list are : ',b)
print('The float type items in list are : ',c)
print('The string type items in list are : ',d)

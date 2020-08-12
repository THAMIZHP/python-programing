'''From the two list obtained in previous question, make new lists,
containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7
and 9 in separate lists.'''

a=list(input('enter the range: ').split())
c,b,d,e,f,g,h,i,j=[],[],[],[],[],[],[],[],[]
for x in range(int(a[0]),int(a[-1])+1):
    if (x%2==0):
        b.append(x)
        if(x%4==0):
            d.append(x)
        if(x%6==0):
            e.append(x)
        if(x%8==0):
            f.append(x)
        if(x%10==0):
            g.append(x)
        if(x%3==0):
            h.append(x)
        if(x%5==0):
            i.append(x)
        if(x%7==0):
            j.append(x)        
    else:
        c.append(x)
        if(x%3==0):
            h.append(x)
        if(x%5==0):
            i.append(x)
        if(x%7==0):
            j.append(x)        
print('The odd list is: ',b,'\n')
print('The even list is: ',c,'\n')
print('The number dived by 4 is: ',sorted(d),'\n')
print('The number dived by 6 is: ',sorted(e),'\n')
print('The number dived by 8 is: ',sorted(f),'\n')
print('The number dived by 10 is: ',sorted(g),'\n')
print('The number dived by 3 is: ',sorted(h),'\n')
print('The number dived by 5 is: ',sorted(i),'\n')
print('The number dived by 7 is: ',sorted(j))




'''Using range(1,101), make two list, one containing all even numbers
and other containing all odd numbers.'''
a=list(input('enter the range: ').split())
c=[]
b=[]
for x in range(int(a[0]),int(a[-1])+1):
    if (x%2==0):
        b.append(x)
    else:
        c.append(x)
print('The odd list is: ',list(b))
print('The even list is: ',list(c))


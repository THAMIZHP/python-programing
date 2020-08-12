'''Initialize a 2D list of 3*3 matrix. E.g.-
1	2	3
4	5	6
7	8	9

Check if the matrix is symmetric or not.'''
t,p=map(int,input('Enter row and column by giving space: ').strip().split())
a=[]
c=0
if(t==p):
    for x in range(t):
        a.append(list(map(int,input('Enter rows of 2D list": ').strip().split()))[:p])
    print(a)
    for x in range(t):
        for y in range(p):
            if (a[x][y]!=a[y][x]):
                c+=1
    if c==0:
        print('Symmentric')
    else:
        print('Not Symmentric')
else:
    print('Not a Square matrix')

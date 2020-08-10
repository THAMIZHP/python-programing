'''Print the following pattern using for loop
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
a=int(input('enter a number: '))
for x in range(a,0,-1):
    for y in range(x,a-x,-1):
        print(y,end=' ')
    print('\n')
    a-=1

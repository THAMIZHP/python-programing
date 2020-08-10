'''Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
b=int(input(' Enter a number: '))
for x in range(1,b+1):
    for y in range(1,x+1):
        print("%d"%(y),end=' ')
    print('\n')

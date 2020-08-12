'''Take inputs from user to make a list. Again take one input from user
and search it in the list and delete that element, if found. Iterate over
list using for loop.'''
#method 1 using remove
a=list(input('Enter a List: ').split())
b=input('What to search in list : ')
if b in a:
    #a.remove(b)
    print(a[b])
else:
    print('Not in List')

#method 2 using pop
a=list(input('Enter a List: ').split())
b=input('What to search in list : ')
if b in a:
    a.pop(a.index(b))
    print(a)
else:
    print('Not in List')

#method 3 using del
a=list(input('Enter a List: ').split())
b=input('What to search in list : ')
if b in a:
    del a[a.index(b)]
    print(a)
else:
    print('Not in list')

#method 4 using for
a=list(input('Enter a List: ').split())
b=input('What to search in list : ')
c=0
d=1
if b in a:
    for x in range(a.index(b),len(a)):
        if(x!= len(a)-1):
            a[x]=a[x+1]
            
            if((x+1)== (len(a)-1)):
               print(a[:(len(a)-1)])
               break
        else:                            #(x == (len(a)-1)):
            print(a[:(len(a)-1)])
else:
    print('Not in list')

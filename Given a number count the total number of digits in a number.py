'''Given a number count the total number of digits in a number'''

a=int(input('enter a number: '))
c=0
for x in range(100):
    b=divmod(a,10)
    c=c+1
    if(b[0]<10):
        c=c+1
        print(c)
        break
    a=a/10

# or this method
a=input('enter a number: ')
print(len(a))

#or using only operator method
a=int(input('enter a number: '))
c=0
for x in range(50):
    if(a>10):
        a=a/10
        c=c+1
    else:
        c=c+1
        print(c)
        break

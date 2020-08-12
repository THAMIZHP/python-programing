'''Print multiplication table of 14 from a list in which multiplication table
of 12 is stored'''
a1=int(input('enter a table for reference: '))
a=list(range(a1,11*a1,a1))
print(a)
b=int(input('enter a  number to show table: '))
#b1=list(range(b,11*b,b))
#print(b1)
c=b-a1
for x in a:
    print(x+c)
    c+=b-a1

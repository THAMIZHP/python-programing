'''
Python: Find the first repeated character of a given string where the
index of first occurrence is smallest
'''

#Solution
t=p=z=0
a=input("Enter a String: ").lower()
for x in a:
    p=0
    for y in a:
        if(x==y and t!=p):
            z=z+1
            print("({},{})".format(x,a.index(x)))
            break
        p=p+1
    if(z!=0):
        break
    t=t+1
if(z==0):
    print('None')

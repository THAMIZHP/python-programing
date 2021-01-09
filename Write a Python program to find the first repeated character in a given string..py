'''
Write a Python program to find the first repeated character in a given string.
'''

#Solution
t=p=z=0
a=input("Enter a String: ").lower()
for x in a:
    p=0
    for y in a:
        if(x==y and t!=p):
            z=z+1
            print(x)
            break
        p=p+1
    if(z!=0):
        break
    t=t+1
if(z==0):
    print('None')

'''
Write a Python program to find the first non-repeating character
in given string.
input: abcabcdef
output: d
'''

#Solution
z=t=p=tp=0
a=input("Enter a string: ")
a=list(a)
for x in a:
    z=p=0
    for y in a:
       if(x==y and t!=p):
           z=z+1
       p=p+1
    t=t+1
    if(z==0):
        tp=tp+1
        print(x)
        break
if(tp==0):
    print("None")

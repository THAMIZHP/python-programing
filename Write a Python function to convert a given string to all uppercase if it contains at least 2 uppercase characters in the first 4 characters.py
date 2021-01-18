'''
Write a Python function to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters
'''
#Solution

a=input("Enter a string: ")
b=c=d=0
for x in a:
    if(b==4):
        break
    b=b+1
    if (x.isupper()):
        c=c+1
    if(c>=2):
        d=d+1
        print(a.upper())
        break
if(d==0):
    print(a)
        

'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows
the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

#Solution

a=input("Enter a string: ")
z=a.find("not")
x=a.find("poor")
if(z<x and z>0 and x>0):
    print("{}{}{}".format(a[:z],"good",a[x+4:]))
else:
    print(a)

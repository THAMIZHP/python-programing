'''
Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
'''

#Solution
a=input("Enter a String: ")
b,c=a.find('.'),a.find(',')
a=list(a)
a[b],a[c]=a[c],a[b]
print(''.join(a))

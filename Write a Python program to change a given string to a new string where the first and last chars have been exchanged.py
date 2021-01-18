'''
Write a Python program to change a given string to a new string
where the first and last chars have been exchanged.
'''

#Solution
a=input("Enter a String: ")
a=list(a)
a[0],a[-1]=a[-1],a[0]
print("".join(a))

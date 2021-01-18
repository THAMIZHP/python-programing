'''
Write a Python program to remove the nth index character from
a nonempty string
 '''
#Solution
a=input("Enter a string: ")
b=int(input("Enter the index to remove: "))
a=list(a)
a.remove(a[b])
print("".join(a))

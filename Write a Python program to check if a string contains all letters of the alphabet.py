'''
Write a Python program to check if a string contains
all letters of the alphabet.
'''

#Solution
a=input("Enter a string: ").lower()
b=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
if (set(a)>= set(b)):
    print('true')
else:
    print('false')

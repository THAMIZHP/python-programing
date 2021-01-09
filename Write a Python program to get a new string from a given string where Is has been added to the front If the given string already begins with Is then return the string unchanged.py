'''
19. Write a Python program to get a new string from a given string
where "Is" has been added to the front. If the given string already
begins with "Is" then return the string unchanged
'''

#Solution
a=input()
if ('Is'or'is' in a[0:2]):
    print(a)
else:
    print('Is '+a)

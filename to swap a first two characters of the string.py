'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

#SOLUTION

a=input("Enter two string: ").split()
print("{}{},{}{}".format(a[1][:2],a[0][2:],a[0][:2],a[1][2:]))

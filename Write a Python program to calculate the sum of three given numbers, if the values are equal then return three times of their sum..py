'''
18. Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
'''

#Solution
a,b,c=int(input()),int(input()),int(input())
if(a==b==c):
    print(9*a)
else:
    print(a+b+c)

'''
16. Write a Python program to get the difference between a given number
and 17, if the number is greater than 17 return double the absolute difference.
'''

#Solution
a=int(input())
if(a>17):
    print(abs(17-a)*2)
else:
    print(17-a)

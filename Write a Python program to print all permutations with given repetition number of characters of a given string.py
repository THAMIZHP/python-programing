'''
Write a Python program to print all permutations with given
repetition number of characters of a given string.
'''
#Solution
from itertools import product
tp=[]
a=input("Enter the string: ")
b=int(input("Repetition: "))
tp=product(a,repeat=b)
print(list(tp))

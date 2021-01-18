'''
Write a Python program to count the occurrences of each
word in a given sentence.
'''
#Solution
a=input("Enter a sentence").strip('. ').lower().split()
p={}
for x in a:
    p[x]=a.count(x)
print(p)    

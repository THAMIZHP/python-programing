'''
 Write a Python program to count and display the vowels of a given text.
 '''
#Solution
a=input("Enter a string: ").lower()
b=['a','e','i','o','u']
c,d=[],0
for x in a:
    if x in b:
        if x not in c:
            c.append(x)
        d=d+1
print(c,d)
        

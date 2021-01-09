'''
Giving a String, write a Python program to find maximum run of
uppercase characters.

Examples:

Input : test_str = ‘GeEKSForGEEksISBESt’ 
Output : 5 
Explanation : ISBES is best run of uppercase.

Input : test_str = ‘GeEKSForGEEKSISBESt’ 
Output : 10 
Explanation : GEEKSISBES is best run of uppercase.
'''

#Solution
a=input("Enter a string")
t=0
p=0
tp=0
for x in a:
    if(x.isupper()):
        if(p>0):
            t=0
            p=0
        t=t+1
        if(t>tp):
            tp=t
    else:
        p=p+1
print(tp)

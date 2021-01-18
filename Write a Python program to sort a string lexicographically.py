'''
Write a Python program to sort a string lexicographically
'''
'''
#Solution
a=input("Enter a String: ")
t,p=[],[]
for x in a:
    if(x.isalpha()):
        t.append(x)
    elif(x.isdigit()):
        p.append(x)
        
print(sorted(p)+sorted(t))

'''
#or

a=input("Enter a String: ")
print(sorted(list(a)))

        

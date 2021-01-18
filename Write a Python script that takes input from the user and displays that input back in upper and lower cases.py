'''
Write a Python script that takes input from the user and displays
that input back in upper and lower cases
'''

#Solution
a=input("Enter a sentence: ").split()
p=[]
for x in a:
    if(x.isupper()):
        p.append(x.lower())
    elif(x.islower()):
        p.append(x.upper())
print(" ".join(p))


''' THIS Will leave word which is not fully uppercase or lowercase''' 

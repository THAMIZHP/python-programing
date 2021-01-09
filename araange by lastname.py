'''
Given a list of names, the task is to write a Python program to sort the
list of names by their last name.

Examples:

Input: [‘John Wick’, ‘Jason Voorhees’]

Output: [‘Jason Voorhees’, ‘John Wick’]

Input: [‘Freddy Krueger’, ‘Keyser Söze’,’Mohinder Singh Pandher’]

Output: [‘Freddy Krueger’, ‘Mohinder Singh Pandher’, ‘Keyser Soze’]

Explanation: K< P < S
Input: [‘John Wick’, ‘Jason Wiak’]
'''
# Solution
t=0
def lastname(n):
    a=n.rfind(" ")
    if(t!=0):
    return(n[a+1+t])



a=input("Enter names by using comma(,): ").strip().split(',')
t=""
for y in range(len(a)):
        for z in range(y,len(a)):
            if(y!=z and lastname(a[y])>lastname(a[z])):
                    t=a[y]
                    a[y]=a[z]
                    a[z]=t
            for x in range():         
                elif(lastname(a[y])==lastname(a[z])):
                    t=t+1
print(a)
            


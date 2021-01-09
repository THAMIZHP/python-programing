'''
Write a Python function that takes a list of words and
returns the length of the longest one. Go to the editor
Sample Output:
Longest word: Exercises
Length of the longest word: 9
'''
#Solution
def larger(a):
    y,z=0,0
    for x in a:
        if(y<len(x)):
            y=len(x)
    return y
''' for x in a:
        if (len(a)==y):
            z=x
    return x   '''

a=input("Enter a string: ").split()
b=larger(a)
print("the largest length is : {}".format(b))
            
            

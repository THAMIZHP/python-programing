'''
Write a Python program to count the number of characters
(character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''

# Solution
q=input("Enter a String: ").strip()
def counter(a):
    return(q.count(a))
i={}
for x in q:
    i[x]=counter(x)
print(i)
    

'''You are given with a list of integer elements. Make a new list which will
store square of elements of previous list.'''

#appending in new list, as we can't assgin expression to empty list
a=list(input('Enter a integer elements: ').split())
b=[]
for x in a:
    b.append((int(x)*int(x)))
print(b)

# or using sam list varible to do process
a=list(input('Enter a integer elements: ').split())
for x in a:
    a[a.index(x)]=(int(x)*int(x))
print(a)

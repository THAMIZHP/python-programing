'''Using range(1,101), make a list containing only prime numbers.'''
a=list(map(int,(input("enter a range : ").strip().split())))[:2]
d=[]
for x in range(a[0],a[1]):
    c=0
    for y in range(a[0],a[1]+1):
        if (x%y==0):
            c+=1
    if(c==2):
       print(x,'is a prime')
       d.append(x)
print("The list containing prime numbers in given range are : ",d)
       
            

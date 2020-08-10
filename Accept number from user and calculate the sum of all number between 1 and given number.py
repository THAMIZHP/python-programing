'''Accept number from user and calculate the sum of all number between 1
and given number'''

a=int(input('enter a numbers for range: '))
y=0
for x in range(1,a+1):
    y=y+x
print(y)

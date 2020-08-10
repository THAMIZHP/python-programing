a=int(input('Enter the 4 digit number: '))
b=int(a%10)
b*1000
c=int(a/10%10)
c=b+c*100
d=int(a/100%10)
d=c+d*10
e=int(a/1000)
e=d+e
print(e)

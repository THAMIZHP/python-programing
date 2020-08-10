ly=int(input())
if(ly%100==0):
    if(ly%400==0):
        print(ly,'is a leap year')
    else:
        print(ly,'is not a leap year')
else:
    if(ly%4==0):
        print(ly,'is leap year')
    else:
        print(ly,'is not a leap year')

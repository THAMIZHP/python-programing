ch=int(input('Enter the classes held on total: '))
ca=int(input('Enter the classes attended on total: '))
cap=(ca/ch)*100
print(cap,'% of class attended')
if(cap<75):
    print('He/She not allowed to attend exam')
else:
    print('He/She allowed to attend exam')

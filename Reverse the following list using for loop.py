'''Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]'''

list1=[10,20,30,40,50]
list1.reverse()
print(list1)
#or this method
list1=[10,20,30,40,50]
a=len(list1)
for x in list1:
    print(list1[a-1])
    a-=1

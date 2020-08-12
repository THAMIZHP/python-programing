'''Sorting refers to arranging data in a particular format. Sort a list of
integers in ascending order ( without using built-in sorted function ).
One of the algorithm is selection sort. Use below explanation of selection sort
to do this.
INITIAL LIST :
2	3	1	45	15
First iteration : Compare every element after first element
with first element and if it is larger then swap. In first iteration,
2 is larger than 1. So, swap it.
1	3	2	45	15
Second iteration : Compare every element after second element
with second element and if it is larger then swap. In second iteration,
3 is larger than 2. So, swap it.
1	2	3	45	15
Third iteration : Nothing will swap as 3 is smaller than every element
after it.
1	2	3	45	15
Fourth iteration : Compare every element after fourth element with
fourth element and if it is larger then swap. In fourth iteration, 45 is larger than 15. So, swap it.
1	2	3	15	45
'''

a=list(map(int,input('Enter a list: ').strip().split()))
b=0
for x in range(len(a)):
    for y in range(x,len(a)):
        if (a[x]>a[y]):
            a[x],a[y]=a[y],a[x]         '''b=a[y]
                                        a[y]=a[x]
                                        print(a)
                                        a[x]=b'''
print('The sorted list using selection sort is : ',a)

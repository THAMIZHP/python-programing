'''Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]'''

l=[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for x in l:
    if(x%5==0 and x<=150):
        print(x)

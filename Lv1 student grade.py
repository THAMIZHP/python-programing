#a is the student
a=int(input())
if(a<25):
    print("F")
elif(a>25 and a<45):
    print("E")
elif(a>45 and a<50):
    print("D")
elif(a>50 and a<60):
    print("C")
elif(a>60 and a<80):
    print("B")
elif(a>80):
    print("A")
else:
    print("INVALID")

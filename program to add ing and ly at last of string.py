'''
Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with
'ing' then add 'ly' instead. If the string length of the given string
is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'       hermoineing
'''

#Solution

a=input("Enter a string: ").strip()
if(len(a)>=3):
    if(a[len(a)-3:]=="ing"):       #or if(a[-1:-4:-1]=="gni")
        print("{}ly".format(a))
    else:
        print("{}ing".format(a))
else:
    print(a)

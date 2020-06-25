l=None
s=None
while True :
    num=input("enter the num")
    if num=="done" :
        break
    try :
        n=float(num)
    except :
        print("Invalid Output")
        continue
    if l is None :
        l=n
    elif n>l :
        l=n
    if s is None :
        s=n
    elif n<s :
        s=n
print('Maximum is',l)
print('Minimum is',s)

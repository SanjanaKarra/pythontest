def computepay(h,r) :
    if h<=40 :
        pay=h*r
        return pay
    elif h>40 :
        pay=(40*r)+((h-40)*1.5*r)
        return pay

p=computepay(45,10.5)
print(p)

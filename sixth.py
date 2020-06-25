hrs = input('enter the no of hours')
h = float(hrs)
rph = input('enter the rate per hour')
r = float(rph)
if h <= 40 :
    pay = r*h
    print('pay')
elif h > 40 :
    pay = (r*40)+(1.5*r*(h-40))
    print('',pay)

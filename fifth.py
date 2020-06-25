num = input('enter the number')
try:
    ival = int(num)
except :
    ival = -1
if ival > 0 :
    print('nicely done')
else :
    print('not a number')
print('all done')

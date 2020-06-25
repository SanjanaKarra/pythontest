fname=input('enter the filename:')
fh=open(fname)

for lx in fh:
    line=lx.rstrip()
    print(line.upper())

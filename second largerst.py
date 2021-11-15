z=[5,1,9,6,1]
print('Array:',z)
maxx=z[0]
smax=z[0]
for i in z:
    test=True
    if i>maxx:
        smax=maxx
        maxx=i
        test=False
    if test and i>smax: smax=i
print('Result:',smax)
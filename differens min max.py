z=[5,1,9,6,1]
print('Array:',z)
maxx=z[0]
minn=z[0]
for i in z:
    if i>maxx: maxx=i
    if i<minn: minn=i
print('Result:',maxx-minn)
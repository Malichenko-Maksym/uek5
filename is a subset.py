x=[5,4,3,101]
y=[4,2,5,1,5,3,7,101]
t=0
for i in range(len(x)):
    if x[i] in y: t+=1
if (i+1)==t:
    print('Is a subset')
else:
    print('Not a subset')
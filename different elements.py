x=[4,36,12,28,5,1,1,1,1,36,9,44,5]
y=[5,1,36,4]
z=[]
for i in x:
    T=True
    for j in y:
        if i==j: T=False
    if T: z=z+[i]   
print(*z)
    
z=[2,3,2,5,8,1,9,8]
print("array:",*z)
x=[]
for i in range(len(z)):
    k=0
    for j in range(len(z)):
        if z[i]==z[j]: k+=1
    if k<2: x=x+[z[i]]
print("Unique elements:",*x)
        
    
    
    

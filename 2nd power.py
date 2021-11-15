arr=[8,2,5,1,9]
arr_1=[]
print("Array:",*arr) 
for i in arr:
    arr_1=arr_1+[i**2]
print("2nd power:",*arr_1)
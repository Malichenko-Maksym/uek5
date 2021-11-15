arr=[15, 8, 31, 47, 2, 19]
arr_1=[]
print("existed array: ",*arr) 
for i in range(len(arr)-1,-1,-1):
    arr_1=arr_1+[arr[i]]
print("reverse array: ",*arr_1)
    
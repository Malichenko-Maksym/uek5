def ret(arr):
   k=''
   for i in arr:
       k=k+str(i)+','
   return k
x=[5,4,3,2,6,5]
print('Array:',x)
print('String:',ret(x))
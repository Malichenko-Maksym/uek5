def median(array):
    if len(array)%2==0:
        return ((array[(len(array)-1)//2]+array[(len(array)-1)//2+1])/2)
    else: return array[len(array)//2]
z=[1,0,9,4,6]
print('a)',z)
print('mediana:',median(z))
x=[6,8,5,3,1,5,0,5,7,6]
print('b)',x)
print('mediana:',median(x))
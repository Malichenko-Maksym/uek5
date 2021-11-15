def minmax(array):
    maxx=array[0]
    minn=array[0]
    for i in array:
        if i>maxx: maxx=i
        if i<minn: minn=i
    return [minn,maxx]
x=[4,2,8,4,7,9,5]
print('Array:',x)
print('Result:',minmax(x))


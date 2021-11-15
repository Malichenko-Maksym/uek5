def bubblesort(array):
    k=0
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                k=array[i+1]
                array[i+1]=array[i]
                array[i]=k
            if array[len(array)-2]>array[len(array)-1]:
                k=array[len(array)-1]
                array[len(array)-1]=array[len(array)-2]
                array[len(array)-2]=k
    
    return array
z=[4,12,6,22,7,9,3,57]
bubblesort(z)
print(*z)
k=[9674,252,532,235,656,267,3567,266436,757357,26426427,5535737,2476475754,65847]
bubblesort(k)
print(*k)
t=[54,23,21,20,15,12,10,5,4,2,1,0]
bubblesort(t)
print(*t)
         
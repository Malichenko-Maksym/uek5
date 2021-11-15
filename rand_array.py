import random
def rand_elem(array):
    x=random.randrange(len(array))
    return array[x]
array=[4,2,5,1,5,3,7,101]
for i in range(3):
    print(rand_elem(array), end=' ')
x=int(input('list size?'))
arr=[]
for i in range(x):
    arr.append(int(input(f'enter {i+1} element ')))
even=[]
odd=[]
for i in arr:
    if i%2==0: even=even+[i]
    else: odd=odd+[i]
print(*even, *odd)
    
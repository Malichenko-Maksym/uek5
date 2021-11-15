z=[1,0,9,4,6]
while True:
    try:
        x=float(input('value: '))
    except:print('Not float')
    else:break
s=0
for i in z:
    if i>x: s+=1
print(f'number of elements greater than {x}: {s}')
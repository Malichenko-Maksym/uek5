def occurs(number, array):
    for i in array:
        if number==i: return True
    return False

while True:
    try:x=int(input('Number: '))
    except:print("Not float, try again")
    else:break
ar=[15, 38, 7, 23, 14]
print("Array:",*ar)
print(f"Result: number {x}", end='')
if occurs(x,ar):print(' appears in the array')
else: print(' not appears in the array')

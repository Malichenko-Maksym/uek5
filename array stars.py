def star(n):
    return '*'*n
x=[12, 6, 4, 9,3,10]
for i in x:
    print(f'{i}:'.rjust(3),star(i))
    
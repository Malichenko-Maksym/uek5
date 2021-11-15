colors=['red','green','white','yellow','pink']
with open("colors.txt", 'a') as f:
    for i in colors:
        print(i, file=f)
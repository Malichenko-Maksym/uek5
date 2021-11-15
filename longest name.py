arr=['Genowefa', 'Onufry', 'Celestyna',' Alojzy',' Pankracy']
print("Names:",*arr)
lon=arr[0]
for i in arr:
    if len(i)>len(lon):
        lon=i
print("Longest name:",lon)
import array as arr 
values =arr.array('i',[1,2,3,4,5,6])
newArr = arr.array(values.typecode,(a for a in values))

for e in newArr:
    print(e)
    
numbers = arr.array('i',[89,54,34,90,23])
print("--------- Array before changing indexes ---------") 
for val in numbers:
    print(val)
numbers[0]=65
numbers[3]=11

print("--------- Array after changing indexes ---------") 

for val in numbers:
    print(val)
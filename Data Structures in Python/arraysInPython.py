import array as arr    #importing array module
values =arr.array('i',[1,2,3,4,5,6])
newArr = arr.array(values.typecode,(a for a in values))

for e in newArr:
    print(e)
    
numbers = arr.array('i',[89,54,34,90,23])
print("--------- Array before changing indexes ---------") 
for val in numbers:
    print(val)
    #Changing the index values of the array
numbers[0]=65
numbers[3]=11

print("--------- Array after changing indexes ---------") 

for val in numbers:
    print(val)
    
    
print("Last element of array :",numbers[-1])
print("Second last element of the array :",numbers[-2])

#deleting the element of array 
del numbers[-1]

#elements after deleting the last element of array
for num in numbers:
    print(num)
    
#concatenation of arrays    

array1 = arr.array('d',[1.2,3.4,5.6,7.8])
array2=arr.array('d',[67.9,63.77])
array3=arr.array('d')
c = array1+array2
print("Array c =",c)

#finding the length of the array

print("Length of array1 : ",len(array1))
print("Length of array2 :",len(array2))
print("Length of numnbers array : ",len(numbers))
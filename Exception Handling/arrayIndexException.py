list1 = [1,2,3,4,5,6]
try:
    print("First element of list :",list1[0])
    print("Second element of list :",list1[1])
    print("Second element of list :",list1[9])      #This line will give arrayindexOutOfBound exception
except:
    print("An error occurred !!")               #This line will get executed after occurance exception
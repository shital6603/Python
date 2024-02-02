x= int(input("Enter first value :"))
y= int(input("Enter second value :"))
try:
    z= x/y
except:
    print("division by zero occurred !!!")
    z=None
print(z)
    
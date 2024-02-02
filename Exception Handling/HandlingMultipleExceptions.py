num1 = int(input("Enter value of first number :"))
num2 = int(input("Enter value of second number :"))
try:
    z=num1/num2
except Exception as e:
    print(e," occurred!")
    z=None
print(z)
    
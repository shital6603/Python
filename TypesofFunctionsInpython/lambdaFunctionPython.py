#Normal function
def cube(y):
    return y*y*y

#lambda function
var = lambda y : y*y*y

square =lambda a:a*a
print("Cube :",cube(5))
print("Cube using lambda function ",var(6))
print("Square using lambda function ",square(9))
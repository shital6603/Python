def function1(a,b):
    try:
        c=((a+b)/(a-b))
    except:
        print("Error occured!")
    else:
        print(c)
        pass
        
function1(3.0,2.0)
function1(3.0,3.0)
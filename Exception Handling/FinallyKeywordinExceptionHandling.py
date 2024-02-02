def exhandFunn():
    try:
        b=10/0
    except Exception as ex:
        print(ex)
    else:
        print("Everything is Fine!!!")
    finally:
        print("This will always get executed !!!")
        
exhandFunn()
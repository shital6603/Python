try :
    fileptr=open("python.txt",'a')
    fileptr.write("Python has so much libraries that can be used for Data sciece!!!")
finally:
    fileptr.close() 
with open("python.txt",'r') as f:
    content = f.read()
    print(content)
    
with open("python.txt",'w') as f:
    wr=f.write("Hello python !!")
    print(wr)
    
with open("python.txt",'r') as f:
    content = f.read()
    print(content)    
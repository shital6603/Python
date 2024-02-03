#This file shows the operations on the file.

fileptr = open("python.txt",'w')            #opening a file
if fileptr:
    print("File opened Successfully !!")
    
    
filecontent=["Python is a versatile programming language!!.","Pyhon os interpreted Programming language!!"]
fileptr.writelines(filecontent)             #writeing the list content in file using writelines function

for i in filecontent:                       #printing the content of the file
    print(i)
    
fileptr.write=("This is textual file where texts can get added !!!!");

fileptr.close()
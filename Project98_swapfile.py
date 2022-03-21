def swapfilefunction():
    file1=input("Enter file name:")
    file2=input("Enter replacing file name:")
    a=open(file1,"r")
    data_a=a.read()
    b=open(file2,"r")
    data_b=b.read()
    a=open(file1,"w")
    data1=a.write(data_b)
    b=open(file2,"w")
    data2=b.write(data_a)
    print("DATA REVERSED SUCCESSFULLY")


swapfilefunction()

'''
a=open(file1,"r")
    data_a=a.read()
    a=open(file1,"w")
    data_a=a.write(data_b)
    b=open(file2,"r")
    data_b=b.read()
    b=open(file2,"w")
    data_b=b.write(data_a)'''


'''file = open("sample.txt","a")
L = ["str1\t", "str2\t", "str3\t"]
file.writelines(L)  '''


def wordCount():
    fileName = input("Enter file name:")
    file = open(fileName,"r")
    data=file.read()
    mylist=data.split()
    wordCount=len(mylist)
    print("Number of words in the file",wordCount)


wordCount()

def wordCount2():
    fileName = input("Enter file name:")
    file = open(fileName,"r")
    lines=file.readlines()
    wordCount=0
    for line in lines:
        words=line.split()
        wordCount+=len(words)
    print("Number of words",wordCount)    

wordCount2()
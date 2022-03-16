usersentence=input("Enter any sentence")
#print(usersentence)
characterCount=0
wordCount=1

for i in usersentence:
    characterCount+=1
    if i==" " :
        wordCount+=1
        characterCount-=1

print("Number of Characters :",characterCount)
print("Number of Words :",wordCount)
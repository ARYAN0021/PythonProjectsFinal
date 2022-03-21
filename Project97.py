# to import random package
import random as rand

level=input("Select your level : EASY HARD \n")

if level == "EASY" :
    number=rand.randint(1,10)
    print("Number Guessing game")
    print("Guess number between (1 to 9)")
elif level == "HARD" :
    number=rand.randint(1,100)
    print("Number Guessing game")
    print("Guess number between (1 to 100)")
else:
    number=rand.randint(1,10)
    print("Number Guessing game")
    print("Guess number between (1 to 9)")
     

# variables
chanceCount=0


#while loop
while chanceCount < 5:
    guess=int(input("Enter your guess:"))
# decision making
    if guess < number :
        print("Entered number was too low : Enter number higher than",guess)
        chanceCount+=1
    elif guess > number :
        print("Entered number was too high : Enter number lower than",guess)
        chanceCount+=1
    elif guess == number :
        print("YOU WIN!!")
        break

if not chanceCount < 5:
    print("YOU LOSE")
    print("CORRECT NUMBER IS",number)



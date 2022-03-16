# to import random package
import random as rand

# variables
number=rand.randint(1,10)
chanceCount=0

print("Guess number between (1 to 9)")
guess=int(input("Enter your guess:"))

#while loop
while chanceCount < 4:
# decision making
    if guess < number :
        print("Entered number was too low : Enter number higher than",guess)
        guess=int(input("Enter your guess:"))
        chanceCount+=1
    elif guess > number :
        print("Entered number was too high : Enter number lower than",guess)
        guess=int(input("Enter your guess:"))
        chanceCount+=1
    elif guess == number :
        print("YOU WIN!!")
        break

if not chanceCount < 4:
    print("YOU LOSE")


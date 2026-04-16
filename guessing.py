import random
print("Welcome to number guessing game!\n Lets Start")
secret=random.randint(1,100)
guess=int(input("Guess a no\n"))
if guess==secret:
    print("YOU WON")
else:
    print("BETTER LUCK NEXT TIME IT'S" , secret)

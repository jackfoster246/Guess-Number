#Guess the number between 1 and 100. We will tell you to guess higher or lower.
import random

print("Guess the random number between 1 and 100!")
random_number = 0
random_number = random.randint(1,100)
user_guess = 0
user_guess = int(input())
while True:
    if(user_guess == random_number):
        print("You got it!")
        break
    
    if(user_guess > random_number):
        print("Try lower!")
    
    if(user_guess < random_number):
        print("Try higher!")
    print("What's your next guess?")
    user_guess = int(input())
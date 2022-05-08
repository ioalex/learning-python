import random

min = 0
max = 1000

print("Welcome!")
print("The instructions are simple!")
print("You will have to guess the number that we're thinking of!")
print("The number will be between 0 and 1000")
print("We will tell you if your guess is higher or lower than our number")
print()
print("Please type 'yes' to play and start guessing!")

play = str(input())
play = play.lower()

number = random.randint(min,max)

while play == "yes":    
    guess = int(input())
        
    if guess > number:
        print("Lower")
        
    if guess < number:   
        print("Higher")
        
    if guess == number:
        print("Congratulations! You are correct!")
        print("To play again, please type 'yes'")
        play = str(input())
        play = play.lower()

if play!= "yes":
    print("Sorry! We couldn't quite get that!")
    print("Please try again!")


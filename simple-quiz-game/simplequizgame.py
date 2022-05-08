print("Welcome to our Millionaire Trivia!")
print("Answer at least 8 questions correctly for our grand prize of $1,000,000!")
print("Please answer the questions by typing A, B, C or D")

ans = input("Are you ready to play? (yes/no) ")

score = 0
totalq = 10

if ans.lower() == "yes":
    print("1. What country is sushi from?")
    print("A: Thailand")
    print("B: Japan")
    print("C: India")
    print("D: France")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("2. According to the Old Testament, how many days did it take God to create the world?")
    print("A: 1")
    print("B: 6")
    print("C: 7")
    print("D: 11")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("3. Which is the world's most populous country?")
    print("A: China")
    print("B: USA")
    print("C: India")
    print("D: Brazi")
    ans = input("Please type your answer ")
    if ans.lower() == "a":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("4. About what percentage of the earth's surface is water?")
    print("A: 10%")
    print("B: 50%")
    print("C: 70%")
    print("D: 95%")
    ans = input("Please type your answer ")
    if ans.lower() == "c":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("5. Is Washington DC a state?")
    print("A: Yes")
    print("B: No")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("6. When should you take antibiotics?")
    print("A: For viruses")
    print("B: For bacterial infections")
    print("C: Never")
    print("D: Whenever you're sick")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("7. Is it true that the shape of a pregnant belly can help parents predict the sex of their baby?")
    print("A: Yes")
    print("B: No")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("8. Is Africa a country?")
    print("A: Yes")
    print("B: No")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("9. Why are French, Spanish and Italian called Romance languages?")
    print("A: They sound romantic")
    print("B: They have roots in Latin, which was spoken by Romans")
    print("C: They are only spoken by the Romani")
    print("D: They were spread by those who roam")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your current score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your current score is", score)
        print()

    print("10. How many moons does the earth have")
    print("A: 0")
    print("B: 1")
    print("C: 2")
    print("D: 5")
    ans = input("Please type your answer ")
    if ans.lower() == "b":
        print("You are CORRECT!")
        score += 1
        print("Your final score is", score)
        print()
    else:
        print("Sorry buddy! You are INCORRECT!")
        print("Your final score is", score)
        print()

print("Thank you so much for playing!")

mark = (score/totalq) * 100
    
print("You answered", mark, "of the quiz correctly")
if score >= 8:
    print("As your score was", score, "you have qualified for our grand prize!")
    print("You have just won $1,000,000!")
    print("Congratulations!")
else:
    print("As your score was", score, "you have unfortunately not qualified for our grand prize")
    print("Better luck next time!")
    print("Feel free to come back anytime!")

    print()
    print("Quiz questions are from play.howstuffworks.com") 

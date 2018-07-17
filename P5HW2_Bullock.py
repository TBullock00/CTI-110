# CTI-110
# P5HW2: Random Number Guessing Game
# Tanenr Bullock
# 10 July 2018
#


def main():
    import random
    random = random.randint (1, 100)
    print (" ")
    print ("=" * 100)
    print ("Welcome to the guessing game!")
    difficulty = input ("Would you like to play on beginner, easy, intermediate, hard, or impossible? ")

    if difficulty == "beginner" or difficulty == "Beginner":
        beginner(random)

    elif difficulty == "easy" or difficulty == "Easy":
        easy(random)

    elif difficulty == "intermediate" or difficulty == "Intermediate":
        intermediate(random)

    elif difficulty == "hard" or difficulty == "Hard":
        hard(random)

    elif difficulty == "impossible" or difficulty == "Impossible":
        impossible(random)

    else:
        print ("Woops! That isn't a mode!")
        playChoice = 'y'
        playChoice = input ("Would you like to try again? y for yes, n for no ")
        if playChoice == 'y':
            main()
        else:
            print ("Thank you for playing!")    




def beginner(random):
    print (" ")
    print ("You have selected 'Beginner' mode.")
    print ("You will have 30 tries. Good luck!")

    tries = 30
    while tries > 0:
        tries = tries - 1
        print (" ")
        guess = int (input ("What is your guess? "))
        if tries == 0:
            print (" ")
            print ("You have lost :(")
            print (" ")
        elif guess == random:
            print ("Congratulations, you have won!")
            break
        elif guess > random:
            print ("Try again! guess lower!")
            print ("You have", tries, "tries left")
        else:
            print ("Try again! Guess higher!")
            print ("You have", tries, "tries left")
    playChoice = 'y'
    playChoice = input ("Would you like to play again? y for yes, n for no ")
    if playChoice == 'y':
        main()
    else:
        print ("Thank you for playing!")


        

def easy(random):
    print (" ")
    print ("You have selected 'Easy' mode.")
    print ("You will have 20 tries. Good luck!")

    tries = 20
    while tries > 0:
        tries = tries - 1
        print (" ")
        guess = int (input ("What is your guess? "))
        if tries == 0:
            print (" ")
            print ("You have lost :(")
            print (" ")
        elif guess == random:
            print ("Congratulations, you have won!")
            break
        elif guess > random:
            print ("Try again! guess lower!")
            print ("You have", tries, "tries left")
        else:
            print ("Try again! Guess higher!")
            print ("You have", tries, "tries left")
    playChoice = 'y'
    playChoice = input ("Would you like to play again? y for yes, n for no ")
    if playChoice == 'y':
        main()
    else:
        print ("Thank you for playing!")




def intermediate(random):
    print (" ")
    print ("You have selected 'Intermediate' mode.")
    print ("You will have 10 tries. Good luck!")

    tries = 10
    while tries > 0:
        tries = tries - 1
        print (" ")
        guess = int (input ("What is your guess? "))
        if tries == 0:
            print (" ")
            print ("You have lost :(")
            print (" ")
        elif guess == random:
            print ("Congratulations, you have won!")
            break
        elif guess > random:
            print ("Try again! guess lower!")
            print ("You have", tries, "tries left")
        else:
            print ("Try again! Guess higher!")
            print ("You have", tries, "tries left")
    playChoice = 'y'
    playChoice = input ("Would you like to play again? y for yes, n for no ")
    if playChoice == 'y':
        main()
    else:
        print ("Thank you for playing!")


        

def hard(random):
    print (" ")
    print ("You have selected 'Hard' mode.")
    print ("You will have 5 tries. Good luck!")

    tries = 5
    while tries > 0:
        tries = tries - 1
        print (" ")
        guess = int (input ("What is your guess? "))
        if tries == 0:
            print (" ")
            print ("You have lost :(")
            print (" ")
        elif guess == random:
            print ("Congratulations, you have won with", tries, "tries left!")
            break
        elif guess > random:
            print ("Try again! guess lower!")
            print ("You have", tries, "tries left")
        else:
            print ("Try again! Guess higher!")
            print ("You have", tries, "tries left")
    playChoice = 'y'
    playChoice = input ("Would you like to play again? y for yes, n for no ")
    if playChoice == 'y':
        main()
    else:
        print ("Thank you for playing!")


        

def impossible(random):
    print (" ")
    print ("You have selected 'Impossible' mode.")
    print ("You will have 3 tries. Good luck!")

    tries = 3
    while tries > 0:
        tries = tries - 1
        print (" ")
        guess = int (input ("What is your guess? "))
        if tries == 0:
            print (" ")
            print ("You have lost :(")
            print (" ")
        elif guess == random:
            print ("Congratulations, you have won!")
            break
        elif guess > random:
            print ("Try again! guess lower!")
            print ("You have", tries, "tries left")
        else:
            print ("Try again! Guess higher!")
            print ("You have", tries, "tries left")
    playChoice = 'y'
    playChoice = input ("Would you like to play again? y for yes, n for no ")
    if playChoice == 'y':
        main()
    else:
        print ("Thank you for playing!")

main()

def game():

    tryAgain = "no"
    numberOfGuess = 0
    import random
    ranNum = random.randint(1, 10)
    #print(ranNum)
    print("This is the Number Guessing Game.")
    currentGuess = int(input("Guess a number between 1 and 10 (You have 3 Guesses)\nWhat is your guess: "))
    while numberOfGuess < 3:
        if currentGuess == ranNum:
            print("You win!!!! Tacos!!!!")
            break;
        else:
            numberOfGuess+=1
            sortingList = [currentGuess, ranNum]
            sortingList.sort()
            highnumber = sortingList[1]
            lownumber = sortingList[0]
            numberDifference = highnumber - lownumber

            if numberDifference > 2:
                print("You are freezing cold.")
            elif numberDifference == 2:
                print("You are getting warmer.")
            else:
                print("You are burning hot.")

            if numberOfGuess == 1:
                print("You have 2 more guesses")
                currentGuess = int(input("What is you guess: "))
            elif numberOfGuess == 2:
                print("You have 1 more guess")
                currentGuess = int(input("What is you guess: "))
            else:
                print("You Lose! sorry")
    tryAgain = input("Do you want to try again?(yes/no) ")
    if tryAgain == "yes":
        game()
    else:
        print("Good game goodbye.")
game()
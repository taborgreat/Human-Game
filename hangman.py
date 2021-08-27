def game(trainee):
    gameRunning = True
    import random

    word_bank = 'hello', 'jackson', 'superman', 'pipette', 'tabor', 'cabinet', 'elmo', 'cannonball', 'rubber', 'planet'
    theWord = word_bank[random.randint(0, len(word_bank) - 1)]

    theWordList = list(theWord)
    theDash = list(theWord)
    y = len(theWord)

    for x in range(y):
        theDash[x] = '-'

    def intro():
        print(f"Welcome to Intelligence Training! Your word is a {len(theWord)} letter word.")

    lives = len(theWord) + 2

    intro()
    while gameRunning:

        for x in range(y):
            print(theDash[x], end='')

        if theDash == theWordList:
            print("\nYou have guessed the word and won! Good job.")
            gameRunning = 0
            return True

        guess = input("\nEnter a letter guess: ")

        while len(guess) != 1 or guess.isnumeric() or not guess.isalpha():
            print("One LETTER at a time...")
            guess = input("\nEnter a letter guess: ")

        times = theWord.count(guess)

        guessPos = theWord.find(guess)

        if guessPos == -1:
            print("Sorry, that letter is not in the word. ", end="")

            lives -= 1

            if lives <= 0:
                print("\nGAME OVER")
                print(f"The word was: {theWord}")
                gameRunning = 0
                return False
            else:
                print(f"You have {lives} guesses remaining")

        else:
            for x in range(times):
                theDash[guessPos] = guess
                guessPos = theWord.find(guess, guessPos + 1)

            print(f"{guess} was in the word {times} times!\n")

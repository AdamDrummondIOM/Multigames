from random import choice

def DisplayMenu():
    print("Paper + Pen Games")
    print("H for Hangman")
    print("N for Noughts and Crosses")
    print("Q for Quit")





#Hangman is Finished
def Hangman():
    
    word = choice(["festival of code","digital eagles"])

    guessed = []
    wrong = []

    tries = 7

    while tries > 0:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            break

        print("Guess the word:", out)
        print(tries, "chances left")

        guess = input().lower()

        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")
            tries = tries - 1
            wrong.append(guess)

        print()

    if tries:
        print("You guessed", word)
        DisplayMenu()
    else:
        print("You didn't get", word)
        DisplayMenu()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def NoughtsNCrosses():

    def changeFrom1():
        PlayerNo = '2'
        print (PlayerNo)

    def changeFrom2():
        PlayerNo = '1'
        print (PlayerNo)
            
    def printSquare():

        print (N1,"|",N2,"|",N3)
        print ("- | - | -")
        print (N4,"|",N5,"|",N6)
        print ("- | - | -")
        print (N7,"|",N8,"|",N9)

    NnC = True
    N1 = '1'
    N2 = '2'
    N3 = '3'
    N4 = '4'
    N5 = '5'
    N6 = '6'
    N7 = '7'
    N8 = '8'
    N9 = '9'
    printSquare()
    while NnC == True:
        print ("Choose which square to place your mark Player.\n")
        edit = input(">_")
        print (edit)


        if edit == '1':
            if PlayerNo == 1:
                N1 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N1 = 'C'
                printSquare
                changeFrom2()
                                
        elif edit == '2':
            if PlayerNo == 1:
                N2 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N2 = 'C'
                printSquare
                changeFrom2()

        elif edit == '3':
            if PlayerNo == 1:
                N3 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N3 = 'C'
                printSquare
                changeFrom2()

        elif edit == '4':
            if PlayerNo == 1:
                N4 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N4 = 'C'
                printSquare
                changeFrom2()

        elif edit == '5':
            if PlayerNo == 1:
                N5 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N5 = 'C'
                printSquare
                changeFrom2()
                
        elif edit == '6':
            if PlayerNo == 1:
                N6 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N6 = 'C'
                printSquare
                changeFrom2()
                
        elif edit == '7':
            if PlayerNo == 1:
                N8 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N8 = 'C'
                printSquare
                changeFrom2()

        elif edit == '9':
            if PlayerNo == 1:
                N9 = 'X'
                printSquare
                changeFrom1()
            if PlayerNo == 2:
                N9 = 'C'
                printSquare
                changeFrom2()

        else:

            print("Unavailable Slot")

        printSquare()
    
running = True

DisplayMenu()

while running == True:

      menuChoice = input(">_").lower()

      if menuChoice == 'q':
            running = False
            
        #Hangman is finished
      elif menuChoice == 'h':
            Hangman()

      elif menuChoice == 'n':
            NoughtsNCrosses()


      elif menuChoice == 'a':
            addDictionaryItem()

      elif menuChoice == 'd':
            deleteDictionaryItem()

      else:
            print("Invalid menu choice!")




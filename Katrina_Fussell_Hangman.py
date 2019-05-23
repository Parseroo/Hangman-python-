#Katrina Fussell 8A
#April 21, 2017
import turtle
import random

turtle.hideturtle()


#Draws the hangman over and over, making it seem to move.  However, since the turtle is going as fast as it can, and I can't seem to make it run without the screen refreshing until it's done drawing, it looks a little weird and is low quality animation.
def animateHangman():
    turtle.speed(0)
    turtle.right(90)
    turtle.hideturtle()
    for i in range(25):
        turtle.clear()
        Position=121-(i*4)
        turtle.left(90)
        drawStickFigure(Position, 75)
    drawBase()

#this draws the little stick figure guy himself.
def drawStickFigure(StartingX, StartingY):
    turtle.penup()
    turtle.goto(StartingX, StartingY)
    #this draws the head
    turtle.pendown()
    turtle.right(90)
    turtle.circle(5)
    turtle.left(90)
    turtle.penup()
    turtle.forward(12)
    turtle.pendown()
    #This draws the arms
    turtle.right(90)
    turtle.forward(6)
    turtle.right(180)
    turtle.forward(12)
    turtle.right(180)
    turtle.forward(6)
    turtle.left(90)
    #this draws the lower half
    turtle.forward(10)
    turtle.right(45)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(45)

#this draws individual parts of the gallows
def bareStep(step):
    if step==5:
        turtle.forward(50)
    elif step==4:
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(90)
    elif step==3:
        turtle.forward(50)
    elif step==2:
        turtle.forward(50)
        turtle.left(90)
    elif step==1:
        turtle.forward(25)
    elif step==0:
        turtle.left(90)
        turtle.forward(25)
    else:
        print " "

#this draws the gallows as a whole.  I split drawBase and bareStep to make it easier to read.
def drawBase():
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown() 
        turtle.right(180)
        bareStep(5)
        bareStep(4)
        bareStep(3)
        bareStep(2)
        bareStep(1)
        bareStep(0)

#This function picks a random word from a read only file that contains a list of words.  Then it returns the word as a plain string.
def pickWord():
    file=open('/usr/share/dict/words', 'r')
    wordlist = file.readlines()
    file.close()
    length = len(wordlist)
    pick = int(random.uniform(1, length))
    word=wordlist[pick]
    return word.strip()

#This creates a list that contains the information for each word containing each sentence, and whether or not it has been guessed yet.
def createSolution(word):
    solution=[]
    for each in word:
        solution.append([each, "undiscovered"])
    return solution

#This checks whether or not the letter you ask about has been discovered, so that it can print out a blank or the letter.
def isUndiscovered(solution, letter):
    for each in solution:
        if (each[0] == letter):
            return (each[1] == 'undiscovered')
    return True

#this function takes in the list and the letter the person has guessed and tells you if you've guessed it yet.
def setDiscovered(solution, letter):
    for each in solution:
        if (each[0] == letter):
            each[1] = 'discovered'

#This function runs the letter guessing loop for the playing hangman function.  I was starting to have issues with the text wrapping funny because my code was getting too far to the right.  
#I put in a bunch of if statements to see if they'd written a space, or nothing at all, or written more than one letter at a time so that it wouldn't take away lives when they make typos, because that's rather unfair.
def letterGuess(word, solution, lives, guessed):
    while True:
        win = True
        for each in word:
            if isUndiscovered(solution, each):
                print "__ ",
                win = False
            else: 
                print each," ",
        print " "
        if win:
            print "Yay! You won!"
            print " "
            break
        if lives == 0:
            print "You have been hung. "
            print "DIE! "
            animateHangman()
            print "My word was", word
            break
        print "You've guessed", guessed 
        userGuess = raw_input("What letter would you like to guess? ")
        userGuess = user_guess.lower()
        if userGuess == "quit":
            break
        if len(userGuess) > 1:
            print "That's too long to be a letter. "
            continue
        print " "
        if userGuess==" ":
            print "You didn't say anything.  That's no fun."
            continue
        elif len(userGuess)==0:
            print "Please guess."
            continue
        elif userGuess in guessed:
            print "You've already guessed that."
            continue
        guessed.append(userGuess)
        if userGuess in word:
            print "You are correct! "
            print userGuess, "is in my word. "
            print " "
            setDiscovered(solution, user_guess)
            continue
        else: 
            print "That isn't in my word.  If you want to give up, type 'quit' "
            lives = lives-1            
            print "You have", lives, "lives left. "
            bareStep(lives)

#This function plays hangman.  The loop makes it so that you can play multiple games without ever having to restart the program.  
def playHangman():
    print " "
    print "Hi!"
    print "This program can play a word guessing game."
    while True:
        print " "
        playGame = raw_input("Would you like to play? ")
        playGame = play_game.lower()
        print " "
        if len(playGame)==0:
            print "Please say something. "
            continue
        if playGame[0]=="y":
            turtle.clearscreen()
            lives=6
            print "You will start with six lives.  If you guess more than six wrong guesses, you will die.  Try and guess my word by guessing individual letters."
            word = pickWord()
            solution = createSolution(word)
            guessed = []
            print "My word is", len(word), "letters long."
            letterGuess(word, solution, lives, guessed)
        elif playGame[0] == "n":
            print "Okay....  Bye....."
            print " "
            break
        else:
            print "I didn't understand you.  Could you rephrase that? "
            
            
playHangman()

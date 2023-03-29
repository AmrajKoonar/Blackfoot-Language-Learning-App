#2022/11/20


#all import statements
import pygame
import cmpt120image
import drawOne
import random

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

file = open("blackfoot.csv")

#for loop that creates a list out of the cvs file
wordBank = []
for i in file:
  listline = i.strip("\n").split(",")
  wordBank = wordBank + listline

#variables needed before while loop
leaveGame = True
difficulty = 3

#whileloop-if the user enters 4, game ends cause leaveGame is now False thus whileloop shuts down.
while leaveGame:
    #prints main menu every time until game is over
    print("\nMAIN MENU\n", "1. Learn - Word Flashcards\n",
                                                            "2. Play - Seek and Find Game\n",
                                                            "3. Settings - Change Difficulty\n",
                                                            "4. Exit\n")
    userInput = input("Choose an option: ").lower()

    #if user presses 1, Learn part is played.
    if "1" in userInput:
        print("\nLEARN")
        for i in range(difficulty):
            pxlary = cmpt120image.getImage("images/" + wordBank[i] + ".png")
            cmpt120image.showImage(drawOne.
                                            distributeItems
                                            (cmpt120image.getWhiteImage(400,300),pxlary,1))
            playSound(wordBank[i],ENV)
            input(str(i+1) + ". Press enter to continue...")

    #if user pressed 2 play part gets played, nested for loop that goes by roundsX3images
    if "2" in userInput:
        print("\nPLAY\n", "This is a seek and find game. You will hear a word. Count how many of that item you find!")
        howManyRounds = int(input("How many rounds would you like to play? "))
        rounds = howManyRounds

        challengeList = []

        for i in range(difficulty):
            challengeList.append(wordBank[i])

        for i in range(rounds):
            #resets backround
            backround = cmpt120image.getWhiteImage(400,300)
            #randomizes sound/list
            random.shuffle(challengeList)
            for b in range(3):

                randomChoiceMinify = random.randint(0,100)
                randomChoiceMirror = random.randint(0,100)

                pxlary = cmpt120image.getImage("images/" + challengeList[b] + ".png")

                newColorPxlary = drawOne.recolorImage(pxlary,[random.randint(0,229),random.randint(0,229),random.randint(0,229)])

                howManyTimes = random.randint(1,4)

                if randomChoiceMinify % 2 == 0 and randomChoiceMirror % 2 == 0:
                    mirrorMinifyRecolorPxlary = drawOne.mirror(drawOne.minify(newColorPxlary))
                    cmpt120image.showImage(drawOne.distributeItems(backround,mirrorMinifyRecolorPxlary,howManyTimes))
                elif randomChoiceMinify % 2 == 0:
                    minifyRecolorPxlary = drawOne.minify(newColorPxlary)
                    cmpt120image.showImage(drawOne.distributeItems(backround,minifyRecolorPxlary,howManyTimes))
                elif randomChoiceMirror % 2 == 0:
                    mirrorRecolorPxlary = drawOne.mirror(newColorPxlary)
                    cmpt120image.showImage(drawOne.distributeItems(backround,mirrorRecolorPxlary,howManyTimes))
                else:
                    howManyTimes = random.randint(1,4)
                    cmpt120image.showImage(drawOne.distributeItems(backround,newColorPxlary,howManyTimes))

            #plays last sound in challengeList, user will not know its the first item because all 3 items are drawn at the same time
            #i am choosing index 2 but it is still randomized earlier by shuffle command, therefore sound is randomized still
            playSound(challengeList[2],ENV)
            question = int(input("Listen to the word. How many of them can you find? "))

            if howManyTimes == question:
                input("Right! Press Enter to continue.\n")
            else:
                input("Sorry, there were " + str(howManyTimes) + " Press Enter to continue.\n")

    #if user presses 3, settings portion is opened and user can change difficult via input
    if "3" in userInput:
        print("You are currently learning " + str(difficulty) + " words.")
        howManyWords = int(input("How many would you like to learn (3-12)? "))
        if howManyWords > 12 or howManyWords < 3:
            print("Sorry, that's not a valid number. Resetting to 3 words.")
            difficult = 3
        else:
            difficulty = howManyWords

    #if 4 is pressed, leaveGame becomes False, therefore while loop ends and so does the program
    if "4" in userInput:
        print("Goodbye!")
        leaveGame = False

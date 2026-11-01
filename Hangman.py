#Hangman in ASCII wooooo yipee look at me go!
#since it is halloween,the word list will be more halloween themed!
import random;
words = ["ghost","poop","spongebob","patrick the star","gerard way","dihydrogen monoxide","frankenstein","hangman","skeleton","pumpkin","witch","spooky","haloween","cobwebs",
        "werewolf","trick or treat","candy","basket","candle","lantern","monster","costume","toilet","person"
        ,"firefighter","police","cowboy","officer","mask","costume","decoration","spider","skull","zombie","superhero",
        "october","autumn","blood","bones","tombstone","carl sagan","albert einstein","nikola tesla","dracula","friday the thirteenth","black phone","prisoner","knight","video games","rene descartes"
        ,"paper mache","soldier","doctor","harry potter","disney","mickey mouse","donald duck","toy story","chandelier","bat wings","spooky","organ","the flaming lips","young the giant","mustard service","celebrity","monopoly man","socrates",
        "plato","cicero de finibus bonorum et malorum","tome","library","extreme","semicolon","grammatical error","python","thanks hackclub we love u","tung tung tung sahur","smiski","bathtub","waterfall","cest la vie","\"hate. let me tell you how much i've come to hate you since i began to live. there are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. if the word hate were engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate i feel for humans at this micro-instant for you.\"",
        "\"this too shall pass.\"","dear evan hansen","please pineapple you can do this","charizard","isabelle","doctor mario","\"what am i going to fight, huh? the sun?\"","minecraft","\" what is this dragon ball z @55 move he's about to use bro? light that burns the sky? ribombee, please survive, please! if this ribombee actually survives this, goat status, giat status. What is going on right now? man, ribombee!! please don't kill him bro! oh my god! is that a spirit bomb!?!!! it might be good though. ribombe!!!!\"","\"ribombee toughed it out so you wouldn't feel sad!\""];
#alphabet for checking the letters
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessedLetters = [""]
#explaination for some stuff
print("P.S. if inputs do not seem to work, know that I made this in Visual Studio Code.\n If it is being run in Visual Studio Code, run it in the terminal by running the python file. \n Otherwise, it will be run in the output and it will not take inputs from the user.\n\nSince the time is about halloween right now, it will be somewhat halloween themed, think common costumes, media, and general halloween stuff.\nIt won't be all halloween, so expect other words and phrases, famous figures, and some quotes!")
print("\n\nGuess the letters until you get the word or type the word outright to win. youhave 4 lives. good luck!")

#make the guy
def makeGuy(stage,s):
    print("\n\n\u2764\uFE0F lives:")
    print(stage)
    print("\u2605 score:")
    print(s)
    print("\n_____________");
    print("|       |");
    if stage == 4:
        for i in range(5):
            print("|");
    elif stage == -1:
        print("|")
        print("|")
        print("|     \\O/")
        print("|      |")
        print("|      /\\")
    elif stage == 3:
        print("|       O")
        for i in range(4):
            print("|");
    elif stage == 2:
        print("|       O")
        print("|       |")
        for i in range(3):
            print("|");
    elif stage == 1:
            print("|       O")
            print("|      -|-")
            for i in range(3):
                print("|");
    elif stage == 0:
        print("|       O")
        print("|      -|-")
        print("|      /\\")
        for i in range(2):
            print("|");
    print("_____________\n");

#make some nice placeholder stuff, check if a character is a letter if it is its printed as a blank, otherwise it prints and ski[s it]
def placeholder(w):
    placeholderp=""
    isLetter=True
    guessedAlready=False
    for i in w:
        isLetter=True
        guessedAlready=False
        for g in guessedLetters:
            isLetter=True
            if i == g:
                guessedAlready=True
        if guessedAlready == True:
            placeholderp+=i
            placeholderp+=" "
        else:
            for a in alphabet:
                if i == a:
                    placeholderp+="_ "
                    isLetter=True
            if isLetter != True:
                if i==" ":
                    placeholderp+="   "
                else:
                    placeholderp+=i
                    placeholderp+=" "
    return placeholderp

#choose word and make some other variables
word=words[random.randint(0,len(words))];
lives=4
score=0
answerGuessedA = False
wrongA=False
def playrounds():
    score=0
    lives=4
    guessedLetters.clear()
    word=words[random.randint(0,len(words)-1)];
    while lives>0:
        #choose word and make some other variables
        answerGuessedA=False
        wrongA=True
        #make the guy to set up
        makeGuy(lives,score)
        print(placeholder(word))
        print("\nletter and words already guessed:")
        print(guessedLetters)
        print("")
        answer = input("type the letter you wish to enter. if you have a guess for the word, punch it in!\nType here:\n")
        for i in guessedLetters:
            if i == answer:
                answerGuessedA = True
        if len(answer)>1:
            if answer == word:
                score+=1
                makeGuy(-1,score)
                print("\nYou saved hangman!")
                playrounds()
            else:
                lives-=1
                if lives == 0:
                    makeGuy(0,score)
                    score=0
                    print("\nhangman is no more, how could you! >:((\nRewinding...")
                else:
                    print("\nThat was the wrong word, try again!")
        elif answerGuessedA==True:
            print("\n You've already guessed that silly! Try again with something you haven't guessed yet!")
        else:
            for i in word:
                if i == answer:
                    wrongA=False
                    guessedLetters.append(answer)
                    print("\nNice one, guess another, or if you've found all the letters or can make the word, guess it(inclde punctuation and especially quotations and ALL LOWERCASE)")
            if wrongA==True:
                guessedLetters.append(answer)
                lives-=1
                if lives == 0:
                    makeGuy(0,score)
                    score=0
                    print("\nhangman is no more, how could you! >:((\nRewinding...\nThe word was "+word+" by the way")
                else:
                    print("\nThat letter is not in the answer, try again!")
        playrounds()
def playrounds():
    score=0
    lives=4
    guessedLetters.clear()
    word=words[random.randint(0,len(words)-1)];
    while lives>0:
        #choose word and make some other variables
        answerGuessedA=False
        wrongA=True
        #make the guy to set up
        makeGuy(lives,score)
        print(placeholder(word))
        print("\nletter and words already guessed:")
        print(guessedLetters)
        print("")
        answer = input("type the letter you wish to enter. if you have a guess for the word, punch it in!\nType here:\n")
        for i in guessedLetters:
            if i == answer:
                answerGuessedA = True
        if len(answer)>1:
            if answer == word:
                score+=1
                makeGuy(-1,score)
                print("\nYou saved hangman!")
                wonround()
            else:
                lives-=1
                if lives == 0:
                    makeGuy(0,score)
                    score=0
                    print("\nhangman is no more, how could you! >:((\nRewinding...")
                else:
                    print("\nThat was the wrong word, try again!")
        elif answerGuessedA==True:
            print("\n You've already guessed that silly! Try again with something you haven't guessed yet!")
        else:
            for i in word:
                if i == answer:
                    wrongA=False
                    guessedLetters.append(answer)
                    print("\nNice one, guess another, or if you've found all the letters or can make the word, guess it(inclde punctuation and especially quotations and ALL LOWERCASE)")
            if wrongA==True:
                guessedLetters.append(answer)
                lives-=1
                if lives == 0:
                    makeGuy(0,score)
                    score=0
                    print("\nhangman is no more, how could you! >:((\nRewinding...\nThe word was "+word+" by the way")
                else:
                    print("\nThat letter is not in the answer, try again!")
    playrounds()
playrounds()
    




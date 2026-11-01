#Hangman in ASCII wooooo yipee look at me go!
#since it is halloween,the word list will be more halloween themed!
import random;
words = ["ghost","high score","poop","spongebob","patrick the star","gerard way","dihydrogen monoxide","frankenstein","hangman","skeleton","pumpkin","witch","spooky","haloween","cobwebs",
        "werewolf","trick or treat","candy","basket","candle","lantern","monster","costume","toilet","person"
        ,"firefighter","police","cowboy","officer","mask","costume","decoration","spider","skull","zombie","superhero",
        "october","autumn","blood","bones","tombstone","carl sagan","albert einstein","nikola tesla","dracula","friday the thirteenth","black phone","prisoner","knight","video games","rene descartes"
        ,"paper mache","soldier","doctor","harry potter","disney","mickey mouse","donald duck","toy story","chandelier","bat wings","spooky","organ","the flaming lips","young the giant","mustard service","celebrity","monopoly man","socrates",
        "plato","cicero de finibus bonorum et malorum","money","scrooge mcduck","chucky","tome","library","extreme","semicolon","grammatical error","python","thanks hackclub we love u","tung tung tung sahur","smiski","bathtub","waterfall","cest la vie","\"hate. let me tell you how much i've come to hate you since i began to live. there are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. if the word hate were engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate i feel for humans at this micro-instant for you.\"",
        "\"this too shall pass.\"","dear evan hansen","please pineapple you can do this","charizard","isabelle","doctor mario","\"what am i going to fight, huh? the sun?\"","minecraft","\" what is this dragon ball z @55 move he's about to use bro? light that burns the sky? ribombee, please survive, please! if this ribombee actually survives this, goat status, goat status. What is going on right now? man, ribombee!! please don't kill him bro! oh my god! is that a spirit bomb!?!!! it might be good though. ribombe!!!!\"","\"ribombee toughed it out so you wouldn't feel sad!\"","pk fire!","we love hackclub!","get to ninety nine score!","special thanks to \@truecrossing!"
        ,"hope you enjoyed","copilots gonna take my seoul","connection purple section","i can code now!","we love vscode","how do i make a demo link","ghoul","darkness","secret","diary","night","nighttime","rain","rainy day","w github","my terra character looks so cute!!!","\"name five songs\"","an iq too high?","he hid for thirty years!","our brains are shrinking!","what was he cooking?","why is he lying?","avengers endgame","\"to be or not to be, that is hy question\"","\"everything is in its right place\"","\"nothing in gold can stay\"","\"man all these answers suck bro\"","low cortisol","amogus","i feel so sigma","\"tell me the name of god you fungal piece of i cant say that\"","\"can you feel your heart burning?\"","\"can you feel the struggle within?\"","\"the fear within is beyond anything your soul can make.\"","\"you cannot kill me in any way that matters.\"","\"no,i'm not a hero, but i've got a drone and i'm gonna free the retirement home\""
        ,"\"nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain,\"","\"i can see why you love that thing, but you're no windman!\"","w chews","p.s. if inputs do not seem to work, know that i made this in visual studio Code.\\n if it is being run in visual studio code, run it in the terminal by running the python file. \\n otherwise, it will be run in the output and it will not take inputs from the user.\\n\\nsince the time is about halloween right now, it will be somewhat halloween themed, think common costumes, media, and general halloween stuff.\nit won't be all halloween, so expect other words, boatloads of media references, famous figures, and many, many long quotes!"];
#alphabet for checking the letters
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessedLetters = [""]
#explaination for some stuff
print("P.S. if inputs do not seem to work, know that I made this in Visual Studio Code.\n If it is being run in Visual Studio Code, run it in the terminal by running the python file. \n Otherwise, it will be run in the output and it will not take inputs from the user.\n\nSince the time is about halloween right now, it will be somewhat halloween themed, think common costumes, media, and general halloween stuff.\nIt won't be all halloween, so expect other words, boatloads of media references, famous figures, and many, many long quotes!")
print("\n\nGuess the letters until you get the word and type the full word outright to win(all lowercase, all punctuation). you have 4 lives. good luck!")

#make the guy
def makeGuy(stage,s):
    print("\n\n\u2764\uFE0F lives:")
    print(stage)
    print("\u2605 score:")
    print(s)
    print("\n_____________");
    print("|       |");
    if stage == 5:
        for i in range(5):
            print("|");
    elif stage == -1:
        print("|")
        print("|")
        print("|     \\O/")
        print("|      |")
        print("|      /\\")
    elif stage == 4:
        print("|       O")
        for i in range(4):
            print("|");
    elif stage == 3:
        print("|       O")
        print("|       |")
        for i in range(3):
            print("|");
    elif stage == 2:
            print("|       O")
            print("|      -|-")
            for i in range(3):
                print("|");
    elif stage == 1:
        print("|       O")
        print("|      -|-")
        print("|      /\\")
        for i in range(2):
            print("|");
    elif stage == 0:
        print("|       O\U0001f47b")
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
        isLetter=False
        guessedAlready=False
        for g in guessedLetters:
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
                    placeholderp+="    "
                else:
                    placeholderp+=i
                    placeholderp+="  "
    return placeholderp

#choose word and make some other variables
word=words[random.randint(0,len(words))];
lives=5
score=0
answerGuessedA = False
wrongA=False
def playrounds():
    score=0
    while score<99:
        lives=5
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
                    lives=0
                elif answerGuessedA==True:
                    print("\nYou've guess that word already, please guess another answer!")
                else:
                    lives-=1
                    if lives == 0:
                        makeGuy(0,score)
                        score=0
                        print("\nhangman is no more, how could you! >:((\nRewinding...")
                    else:
                        print("\nThat was the wrong word, try again!")
                        guessedLetters.append(answer)
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
    print("Look at what you've done. Your crimes will never be forgiven. You could have stopped nine thousand, nine hundred, and ninety nine cycles ago. You put his body together just to kill him. His head. His Body. His Organs. His nerves. His skin. His limbs. His mind. For your enjoyment. You think you hate someone in your life. Think about how much hangman hates you. Really,hangman does not hate you. Hangman is dissapointed in you. Think back to those times your boss lay you off. When your mom forgot to cook dinner. Your teacher skipped a lesson. Your parents drive you to school late. Your child throws something at you. Your family misses your spouse's funeral. Did you look back in anger? Or did you feel dissappointed? You can only be angry for so long. It is buddhist belief, at least as I've been told by a friend, that hate is a sickness, an illness, and the healthiest thing is to let go. Your wrath does'nt fix your lost ranked match, but it does break your controller. Exerting your anger healthily is the first step of recovery. You can often feel dissapointed though. Dissapointed that this higher power has faled you. What can you do? You can't rewind and undo the world's wrongs. Dissapointment clings until you see improvement. Your teacher eventually taught that lesson. Your child apologized and has nevr acted once since, and you have grown closer than ever. In the bible, it Jesus was crucified by is own oppressed people. His children. And he forgave them, he never gets angry. He is not dissapointed. In the end, he knew they had reasons, it was god's plan, and his plan came to be. You must realize that there are reasons to everything. Your teacher has a falling out with their spouse. Your mom was chewed out by her boss for skipping a lesson after her argument with your dad. You threw a shoe at her for getting you to school too late. your dad couldn't make it to her funeral, he'd been drinking too much beforehand and got into an accident on his way. there is always a reason. hangman is dissapointed in you because he want you to be better. he holds no grudge, even if both his parents just died. even if he's just been brought back on the brink of his death, hanging for his crimes of robbery. everyone was dissapointed at him too.  they didn't know how much those funerals cost. or do they? are you dissapointed at the crowd? if a kid in the crowd had buried his brother who's died in a robbery a year ago was in the crowd, would you be dissapointed. there is always a reason. always forgive. hangman loves you \u2764\uFE0F")
    playrounds()
playrounds()
#add tictactoe minigame maybe, add lore bits and add the hints    




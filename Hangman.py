#Hangman in ASCII wooooo yipee look at me go!
#since it is halloween,the word list will be more halloween themed!
import random;
words = ["ghost","high score","poop","spongebob","patrick the star","gerard way","dihydrogen monoxide","frankenstein","hangman","skeleton","pumpkin","witch","spooky","haloween","cobwebs",
        "werewolf","trick or treat","candy","basket","candle","lantern","monster","costume","toilet","person"
        ,"firefighter","police","cowboy","officer","mask","decoration","spider","skull","zombie","superhero",
        "october","autumn","blood","bones","tombstone","carl sagan","albert einstein","nikola tesla","dracula","friday the thirteenth","black phone","prisoner","knight","video games","rene descartes"
        ,"paper mache","soldier","doctor","harry potter","disney","mickey mouse","donald duck","toy story","chandelier","bat wings","spooky","organ","the flaming lips","young the giant","mustard service","celebrity","monopoly man","socrates",
        "plato","cicero de finibus bonorum et malorum","money","scrooge mcduck","chucky","tome","library","extreme","semicolon","grammatical error","python","thanks hackclub we love u","tung tung tung sahur","smiski","bathtub","waterfall","cest la vie","\"hate. let me tell you how much i've come to hate you since i began to live. there are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. if the word hate were engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate i feel for humans at this micro-instant for you.\"",
        "\"this too shall pass.\"","dear evan hansen","please pineapple you can do this","charizard","isabelle","doctor mario","\"what am i going to fight, huh? the sun?\"","minecraft","\" what is this dragon ball z @55 move he's about to use bro? light that burns the sky? ribombee, please survive, please! if this ribombee actually survives this, goat status, goat status. What is going on right now? man, ribombee!! please don't kill him bro! oh my god! is that a spirit bomb!?!!! it might be good though. ribombe!!!!\"","\"ribombee toughed it out so you wouldn't feel sad!\"","pk fire!","we love hackclub!","get to ninety nine score!","special thanks to @truecrossing!"
        ,"hope you enjoyed","copilots gonna take my seoul","connection purple section","i can code now!","we love vscode","how do i make a demo link","ghoul","darkness","secret","diary","night","nighttime","rain","rainy day","w github","my terra character looks so cute!!!","\"name five songs\"","an iq too high?","he hid for thirty years!","our brains are shrinking!","what was he cooking?","why is he lying?","avengers endgame","\"to be or not to be, that is hy question\"","\"everything is in its right place\"","\"nothing in gold can stay\"","\"man all these answers suck bro\"","low cortisol","amogus","i feel so sigma","\"tell me the name of god you fungal piece of i cant say that\"","\"can you feel your heart burning?\"","\"can you feel the struggle within?\"","\"the fear within is beyond anything your soul can make.\"","\"you cannot kill me in any way that matters.\"","\"no,i'm not a hero, but i've got a drone and i'm gonna free the retirement home\""
        ,"\"nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain,\"","\"i can see why you love that thing, but you're no windman!\"","w chews","p.s. if inputs do not seem to work, know that i made this in visual studio Code.\\n if it is being run in visual studio code, run it in the terminal by running the python file. \\n otherwise, it will be run in the output and it will not take inputs from the user.\\n\\nsince the time is about halloween right now, it will be somewhat halloween themed, think common costumes, media, and general halloween stuff.\nit won't be all halloween, so expect other words, boatloads of media references, famous figures, and many, many long quotes!","\"this? state? this? hit the road dude this aint no state property this is private property\""];

#hints for the hint feature:
hints = ["casper the?",
        "something that poeple reach for",
        "only 2 unique letters in form xyyx",
        "yellow guy from a hit kids show named after him",
        "yellow guy's companion in hit kids show named after yellow guy",
        "have a floating picture of him in your hallway and your shoes will be converted into converses and your pants will be skin tight, a true blessing for some.",
        "dangerous chemical that kills millions yearly",
        "gothic literature beast that titles its hit book by Mary Shelley",
        "what are you looking at?",
        "spooky scary _",
        "can get very large, big enough that there is an event where people use them as boats.",
        "clearing b***** off my property(mega niche hint, censored word is not the answer)",
        "_ month",
        "secretive holiday of celtic origin",
        "unattended corner",
        "rampage in target house, killing visitors of target's house with a power 2 attack, if no target is selected, rampage at home, killing those who visit you.(hint from town of salem)",
        "smell my feet",
        "crush",
        "one of the oldest containers concieved by man.",
        "birthday cake appendage",
        "8 iron nuggets and a torch",
        "something book of something",
        "what parties happen on halloween",
        "throne fit for a king",
        "you",
        "buncha dudes who live in the same house for a living",
        "the rookie",
        "scruggs",
        "police",
        "drama _",
        "jack o lanterns and messy over the top spider webs on someone's house",
        "moves by pumping blood through their legs",
        "this one is in your head your almost there just think a lil harder",
        "they are coming...",
        "metroman",
        "canon event month",
        "when leaves start falling",
        "you have a lot of it",
        "sticks and stones may break these",
        "living",
        "pale blue dot",
        "the liberty torch was snuffed out only for this man",
        "famous inventor that isnt albert einstein",
        "has a big castle",
        "a day considered unlucky by many",
        "popular horror movie",
        "orange jumpsuit",
        "a soldier who serves royalty.",
        "comes before homework",
        "a famous philosopher whose most famous quote is also a word in the word bank",
        "arts and crafts project using paper",
        "another fairly common costume",
        "what many young childrren aspire to be",
        "DID YOU PUT YOUR NAME IN THE GOBLET OF FIRE??!! Dumbledore said calmly",
        "a famous childrens cartoons company",
        "childrens show icon",
        "a slightly less iconic childrens show character",
        "very popular movie series",
        "associated pokemon is a ghost and fire type",
        "i cant come up with a hint for this one good luck",
        "_ month",
        "piano like instrument found in churches",
        "popular 90's psych pop band coming back from a 6 year hiatus with album \"teardrop throbs\" set to release in january 2027",
        "famous multiracial band with origins in inglewood, CA. Their most recent album is about hope in times of war and hardship and the idea of choosing love over hate",
        "growing pop rock band from miami whose band name was generated by a random band name generator",
        "indie shoegaze artist from san diego who has a jawline sharp enough to cut steel",
        "popular people",
        "he doesn't have a monocle?",
        "if vibe coding is your power, then what are you without it?",
        "playdough",
        "book from a famous greek philosopher",
        "something asssociated with the color green.",
        "spirits of future past",
        "scary took waldos shirt",
        "magic book",
        "the building with the most stories",
        "something much more than normal",
        "something used frequently when coding in java",
        "I win this argument",
        "programming language i built hangman in",
        "something we all say when we wake up",
        "guy with a bat at the bus stop at n night",
        "little green figurines from japan",
        "something you throw bombs in",
        "firefly",
        "such is life",
        "good luck you got this (make sure to include all punctuation, especially quotations ALL LOWERCASE, so dont copy paste, ooh that rhymes im gonna be next bruno mars)",
        "old persian saying that can both make sad man happy and a happy man sad with a single phrase",
        "a musical about someone's imaginary friend, the soundtrack is great anf one of the more popular tracks refers to the \"If a tree falls in a forest and no one is around to hear it, does it make a sound?\" thought experiment originating in 1883 about the perception of sound and if objects exist if there is nothing to percieve them.",
        "something i said on my first day of terra",
        "one of the most popular pokemon, whose x mega evolution is often considered to be more than miles cooler than the y mega evolution",
        "one of my mains in smash bros",
        "the best character in smash bros",
        "reference to a popular clip in the hollow knight community",
        "the world's bestselling video game",
        "a very funny pokemon clip i threw in to make you type more",
        "goat status",
        "something you hear a lttle too much",
        "something you say every day when waking up",
        "something you should do",
        "the goat",
        "something i say to you",
        "yeah this happened",
        "homophones of ambigrams of names of pets belonging to underground 80's filipino bands cesar ciphered by their total number of tracks excluding their debut album, missing a letter",
        "i really have the power",
        "something WE say when WE wake up",
        "actually how tho",
        "a kind of zombie thing idk",
        "associated with evil and bad things",
        "something that happens when you get to 99 score",
        "something you don't want people looking through",
        "_ owls",
        "a time when you do not go mining",
        "something world",
        "one of the best things to happen like ever",
        "w github",
        "something about terra, so you can guess those letters",
        "something you hear from rude mean people who want to hurt your feelings",
        "youtube thumbnail with the raven on it",
        "a man kept fighting a war that had already ended for 30 years, refusing to believe that they'd lost and denying those who told him to come home as he was trained to be paranoid and not trust them, he killed many farmers and civillians before his former general had to personally tell him to stop, and only then did he return to his family.",
        "picture with a skull with an arrow pointing at it",
        "innocent farmer grape man was attacked in his house before being brutally murdered",
        "picture of a phone in the foreground and a man looking up at the camera in the background",
        "you should have gone for the head.",
        "william shakespeare said thisprobably",
        "a title of a radiohead song, referenced ",
        "a poem from 1923 by robert frost where the title is the final line. the line is also referenced in two young the giant songs,\'daydreamer\' and \'life is a long goodbye\'",
        "something you'd say if you made it all the way to 99 score",
        "a popular meme from a while ago that is associated with either a dial similar to a pressure gague or a man leaning back surrounded my floating leaves with a green soft smiling emoticon beside him.",
        "a popular whodunnit game popularized 2020 by the pandemic, missing a letter",
        "this is how i was before i knew i had to do another ten on the same project",
        "the fist line of a 2018 tumblr post, from the view of the narrator pointing a gun at a mushroom who responds to the ",
        "from a 2018 tumblr post about a mushroom",
        "from a 2018 tumblr post about a mushroom",
        "from a 2018 tumblr post about a mushroom",
        "from a 2018 tumblr pust about a mushroom",
        "line from \'drone song\', a song from edgehill's first album \'ode to the greyhouse\'.",
        "a line from a famous work by a greek philosopher that inspired a famous piece of filler text used in many websites today.",
        "mega niche reference I dont't expect you to get this one",
        "(new lingo)",
        "instructions",
        "a recorded interaction between a fisher and an elderly man in his truck that went viral on social media"]
#alphabet for checking the letters
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessedLetters = [""]

#checkpoint messages,row 1 is score messages. 0 score is intructions and ps row 2 is stars total
checkpointMessages=[["P.S. if inputs do not seem to work, know that I made this in Visual Studio Code.\n If it is being run in Visual Studio Code, run it in the terminal by running the python file. \n Otherwise, it will be run in the output and it will not take inputs from the user.\n\nSince the time is about halloween right now, it will be somewhat halloween themed, think common costumes, media, and general halloween stuff.\nIt won't be all halloween, so expect other words, boatloads of media references, famous figures, and many, many long quotes!\n\n\nGuess the letters until you get the word and type the full word outright to win(all lowercase, all punctuation). you have 7 lives. good luck!\n\ntype and enter \"help\" for extra info and help!",
                    "5 in a row! you got this! keep going!!",
                    "10 in a row! you're killing it!",
                    "20! I know this game is endless, but there is a special secret at 99 score!",
                    "50! halfway there! look at how far you've come!",
                    #67 score
                    "can't escape it",
                    "three quarters the way there!",
                    "one hundred. your first of many. there is more beyond this, though. keep going!",
                    "150, this is my first python project on vscode, and the first personal project ive done on vs code. thanks for being so kind as to stay for so long! have some cake!\n\U0001F382",
                    "200. two hundred cycles. you can't just stop there, more awaits at the 1000 mark!",
                    "five. hundred. cycles. half way there. you can do this!"
                    "Look at what you've done. You could have stopped a hundreds of cycles ago. all the previous messages were fake. there is no loving family. there is no children. there is no wife. You put his body together just to kill him. His head. His Body. His Organs. His nerves. His skin. His limbs. His mind. For your enjoyment. You think you hate someone in your life. Think about how much hangman hates you. Really,hangman does not hate you. Hangman is dissapointed in you. Think back to those times your boss lay you off. When your mom forgot to cook dinner. Your teacher skipped a lesson. Your parents drive you to school late. Your child throws something at you. Your family misses your spouse's funeral. Did you look back in anger? Or did you feel dissappointed? You can only be angry for so long. It is buddhist belief, at least as I've been told by a friend, that hate is a sickness, an illness, and the healthiest thing is to let go. Your wrath does'nt fix your lost ranked match, but it does break your controller. Exerting your anger healthily is the first step of recovery. You can often feel dissapointed though. Dissapointed that this higher power has faled you. What can you do? You can't rewind and undo the world's wrongs. Dissapointment clings until you see improvement. Your teacher eventually taught that lesson. Your child apologized and has nevr acted once since, and you have grown closer than ever. In the bible, it Jesus was crucified by is own oppressed people. His children. And he forgave them, he never gets angry. He is not dissapointed. In the end, he knew they had reasons, it was god's plan, and his plan came to be. You must realize that there are reasons to everything. Your teacher has a falling out with their spouse. Your mom was chewed out by her boss for skipping a lesson after her argument with your dad. You threw a shoe at her for getting you to school too late. your dad couldn't make it to her funeral, he'd been drinking too much beforehand and got into an accident on his way. there is always a reason. hangman is dissapointed in you because he want you to be better. he holds no grudge, even if both his parents just died. even if he's just been brought back on the brink of his death, hanging for his crimes of robbery. everyone was dissapointed at him too.  they didn't know how much those funerals cost. or do they? are you dissapointed at the crowd? if a kid in the crowd had buried his brother who's died in a robbery a year ago was in the crowd, would you be dissapointed. there is always a reason. always forgive. hangman loves you \u2764\uFE0F"],
                    ["your first star, get more to get secret dialogues and messages :P",
                     "5 stars, what a pro :O!",
                     "10 stars. is this even hard for you?",
                     "20 stars? added hints because I thought it'd be too hard, but maybe i didn't",
                     "40 \u2B50 ?! if you are a terra reviewer, Its crazy you made it this deep! there isn't much special about this one, so i don't think any terra reviewer or anyone for that matter will see most of my monologues. i thought reviews were supposed to last less than 2 minutes, so you should probably move on. thank you for playing!",
                     "50 stars!!! thats like, half of 100!",
                     "really, why are you still here? to be fair, a good amount of secrets are left in for the star streaks, but there are some for 90 and 100 stars.",
                     "hangman, the character you see on your screen, is married with two children, named ratticus and heidi. his favorite meal is cheesed cauliflower on a winter day, and his favorite weather is sunny fall/winter days with some clouds to watch, as he loves watching clouds. he works as a mailboy and chef for a local restaurant. he drives a jeep and is a family man, speding as much time as he can with his family.",
                     "100 stars... I'd say you've reached rockstardom, but true rockstardrom awaits at 99 star streak!"],
                     ["So you've made it with barely a single mishap. if you've seen the message from 999 score, theres no worry this time. hangman doesn't feel anything until you use a hint or introduce one of his limbs. your stars broke his seal. really, he is awake. it was all one bad dream. hangman thanks you for breaking him out of his torture. he is going back to watch clouds with his family, and yes, his mom and dad are fine. he has a drone, maybe he'll free the retirement home! i really like that line. you've dunnit! you've hit TRUE rockstardom! we are very proud of you, though you should probably, definitely take a break from screens, touch some grass and stretch. thanks for playing!!! (future runs are played with a hang-man doll, a new toy they started making after you spread your story to the masses. the ghost is replaced with heidi in costume.) have a good day, and remember to always love!",
                     "3 stars in a row! you really are good at this!",
                     "5 stars in a row, a faint glow emanates somewhere in the tremulous fields..",
                     "10 stars in a row, you are filled with determination",
                     "15 stars in a row, rockstardom awaits.",
                     "you should take a break and stretch. seriously. 20 streak is probably enough for now.",
                     "50. wow. are you cheating? ",
                     "75 streak. My mains in smash bros are isabelle, dr mario and corrin, though i play a fair share of other characters, though i don't get a lotta playtime on it, i don't have a switch. remember to drink water! water is very good for you.",
                     "90. you might be able to free hang man if you get a high enough streak.",
                     "its a little too late.. hang man has already suffered a thousand cycles. mind scrambled, mind frayed, mind blank. he's woken up, but he'll never be the same again. he is a vegetable. he is healing and has hopes to make a full recovery soon, future rounds are played on the hospital monitor.",
                     "he has recovered, and is living happily with his family. but nothing in gold can truly stay.",
                     "\"hey... i don't remember buying that lamp.\" hangman says as he stares at the lamp on his nightstand, but he realizes it looks does not look right, it is almost flat, fuzzy around the edges, and the color shifts oddly. he has been staring at it for 2 days. he can't take his off it. his family tries, and to no avail, to break his trance. and he woke up. he is on that rope again, with both his legs missing. it was just a dream. he didn't have his family. his \"wife\" is in that crowd, just like everyone else. he was the one who stole from her, after all. you bought him that sweet relief, but only for so long. maybe if your streak was just a bit higher that first time, he'd be here. maybe you can save him, next time, without ever breaking that streak. he doesn't know what's real, he can't trust what he knows. good luck."]
                     ]

#get variables for making the box
boxTop="\n"
for i in range(134):
    boxTop +="\u2501"
boxTop+="\u256E\n"

boxBottom="\n\n"
for i in range(134):
    boxBottom+="\u2501"
boxBottom+="\u256F"
print(boxTop)
#explaination for some stuff
print("")
print("")

#make the guy
def makeGuy(stage,s,h,hs,st,sts):
    print(boxTop)
    hin=""
    if h:
        hin="yes"
    else:
        hin="no"
    print("\u2764\uFE0F  lives: "+str(stage)+"\t\u2022 score: "+str(s)+"\t\U0001F4A1hint available: "+hin+"\t\U0001F494 hints used: "+str(hs)+"\t\u2B50 stars: "+str(st)+"\t\U0001F320 star streak: "+str(sts))
    print("\n_____________");
    print("|       |");
    if stage == 7:
        for i in range(5):
            print("|");
    elif stage == -1:
        print("|")
        print("|")
        print("|     \\O/")
        print("|      |")
        print("|      /\\")
    elif stage == 6:
        print("|       O")
        for i in range(4):
            print("|");
    elif stage == 5:
        print("|       O")
        print("|       |")
        for i in range(3):
            print("|");
    elif stage == 4:
            print("|       O")
            print("|      -|")
            for i in range(3):
                print("|");
    elif stage == 3:
        print("|       O")
        print("|      -|-")
        for i in range(3):
            print("|");
    elif stage == 2:
        print("|       O")
        print("|      -|-")
        print("|      /")
        for i in range(2):
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
#checkpoint message system
def checkpointM(score,star,streak):
    row=-1
    col=-1
    if score==5 or score==10 or score==20 or score==50 or score==100 or score==200 or score==500 or score==150 or score==67 or (score==999 and streak!=999) or (score==999 and streak==999):
        row=0
        if score==5:
            col=1
        elif score==10:
            col=2
        elif score==20:
            col=3
        elif score==50:
            col=4
        elif score==67:
            col=5
        elif score==75:
            col=6
        elif score==100:
            col=7
        elif score==150:
            col=8
        elif score==200:
            col=9
        elif score==500:
            col=10
        elif score==999:
            col=11
        print(checkpointMessages[row,col])
    if star==1 or score==5 or score==10 or score==20 or score==40 or score==50 or score==75 or score==90 or score==100:
        row=1
        if star==1:
            col=0
        elif star==5:
            col=1
        elif star==10:
            col=2
        elif star==20:
            col=3
        elif star==40:
            col=4
        elif star==50:
            col=5
        elif star==75:
            col=6
        elif star==90:
            col=7
        elif star==100:
            col=8
        print(checkpointMessages[row,col])
    if streak==3 or streak==5 or streak==10 or streak==15 or streak==20 or streak==50 or streak==75 or streak==90 or (streak==999 and score!=999)  or streak==1000 or streak==1001:
        row=2
        if streak==3:
            col=1
        elif streak==5:
            col=2
        elif streak==10:
            col=3
        elif streak==15:
            col=4
        elif streak==20:
            col=5
        elif streak==50:
            col=6
        elif streak==75:
            col=7
        elif streak==90:
            col=8
        elif streak==999 and score!=999:
            col=9
        elif streak==1000:
            col=10
        elif streak==1001:
            col=11
        print(checkpointMessages[row,col])


#choose word and make some other variables
word=words[random.randint(0,len(words))];
lives=7
score=0
answerGuessedA = False
wrongA=False

def playrounds():
    score=0
    hintsUsed=0
    stars=0
    starStreak=0
    while score<99:

        lives=7
        guessedLetters.clear()
        word=words[random.randint(0,len(words)-1)];
        hintUsed=False
        checkpointM(score,stars,starStreak)
        while lives>0:
            print(boxBottom)
            #choose word and make some other variables

            answerGuessedA=False
            wrongA=True
            addedToGList=False
            giveHint=False

            #make the guy to set up
            makeGuy(lives,score,hintUsed,hintsUsed,stars,starStreak)
            print(placeholder(word))
            print("\nletter and words already guessed:")
            print(guessedLetters)
            print("\n")
            answer = input("type the letter you wish to enter. if you have a guess for the word, punch it in!\nType here:\n")
            for i in guessedLetters:
                if i == answer:
                    answerGuessedA = True
            if answer=="hint" and lives>0 and lives<6 and hintsUsed>5:
                hintask=input("\nsay the magic words and try again.\n")
                if hintask=="hint":
                    print("were you expecting something? i told you, say the magic words like this:\"may i have a hint please\" and your wish will be granted! geez, you are so impatient")
                elif hintask=="may i have a hint please":
                    hintasktwo=input("\npunctuation counts, try again!\n")
                    if hintasktwo=="may i have a hint please?":
                        hintaskthree=input("\nI'm not your professor, you don't need to be so formal with me! just say\"hint please!\" like it says in the instructions!\n")
                        if hintaskthree=="hint please!":
                            hintaskfour=input("\nin the instructions, it says to just type and enter \"hint\"! you don't need to be so verbose, we've barely met!\n")
                            if hintaskfour=="hint":
                                giveHint=True
                            else:
                                print("\nwhat did i just say? its in the instructions, just type it in! I'm telling you, no funny business this time!\n")
                        else:
                            print("\nyou should focus on your manners, you know that?\n")
                    else:
                        print("\nlearn proper punctuation and try again >:(\n")
                else:
                    print("\nbad manners? no hint for you!\n")
            if answer=="may i have a hint please" and lives>1 and lives<6:
                hintasktwo=input("\npunctuation counts, try again!\n")
                if hintasktwo=="may i have a hint please?":
                    hintaskthree=input("\nI'm not your professor, you don't need to be so formal with me! just say\"hint please!\" like it says in the instructions!\n")
                    if hintaskthree=="hint please!":
                        hintaskfour=input("\nin the instructions, it says to just type and enter \"hint\"! you don't need to be so verbose, we've barely met!\n")
                        if hintaskfour=="hint":
                            giveHint=True
                        else:
                            print("\nwhat did i just say? its in the instructions, just type it in! I'm telling you, no funny business this time!\n")
                    else:
                        print("\nyou should focus on your manners, you know that?\n")
                else:
                    print("\nlearn proper punctuation and try again >:(\n")
            if answer=="may i have a hint please?" and lives>1 and lives<6:
                hintaskthree=input("\nI'm not your professor, you don't need to be so formal with me! just say\"hint please!\" like it says in the instructions!\n")
                if hintaskthree=="hint please!":
                    hintaskfour=input("\nin the instructions, it says to just type and enter \"hint\"! you don't need to be so verbose, we've barely met!\n")
                    if hintaskfour=="hint":
                        giveHint=True
                    else:
                        print("\nwhat did i just say? its in the instructions, just type it in! I'm telling you, no funny business this time!\n")
                else:
                    print("\nyou should focus on your manners, you know that?\n")
            if answer=="hint please!" and lives >1 and lives<6:
                hintaskfour=input("\nin the instructions, it says to just type and enter \"hint\"! you don't need to be so verbose, we've barely met!\n")
                if hintaskfour=="hint":
                    giveHint=True
                else:
                    print("\nwhat did i just say? its in the instructions, just type it in! I'm telling you, no funny business this time!\n")


            if giveHint==True:
                print("\nyour hint for this word is: \n\n\""+hints[words.index(word,0,len(words))]+"\"")
                hintsUsed+=1
                lives-=1
            elif answer=="help":
                print("Type a letter into the terminal and press enter to guess a letter, once you have all the letters or have a guess for the full word, type it in to guess! \n*****BE SURE TO INCLUDE ALL PUNCTUATIONS, SPACES, etc. NO UPPERCASE LETTERS!!*****\nAfter you have less than 6 lives, you are allowed to exchange a life for a hint by typing \"hint\"! Be careful though, as helpful as some hits can be, many hints are more obscure references and may seem unrelated if you don't catch the reference. \nThere is a mechanic called \"stars\" in this version, requiring you to guess the word without using more than 2 lives. This means you cannot get the star if you need a hint, as the hint will put you at 4 lives, making that round inelligible for the star. there is also a streak counter that counts your consecutive stars.\n there are secret messages at certain checkpoints, 5 score, 10 score, so on. there is also messages associated with stars and most importantly star streaks, which are more or less frequent, be careful and hit those goals!")
            elif len(answer)>1:

                if answer == word:
                    score+=1
                    if lives>4:
                        stars+=1
                        starStreak+=1
                    else:
                        starStreak=0
                    makeGuy(-1,score,hintUsed,hintsUsed,stars,starStreak)
                    print("\nYou saved hangman!")
                    lives=0
                    
                #debug commands, foward slash followed by g for give word, p# for pick word at words[#], s# to make score = #, l to reset lives to max, q# to increase stars by # and w# to increase starStreak by #
                elif answer[0] =="/":
                    if answer[1]=="g":
                        print(word)
                    elif answer[1]=="p":
                        word=words[int(answer[2])]
                    elif answer[1]=="l":
                        lives=7
                    elif answer[1]=="s":
                        score=int(answer[2])
                    elif answer[1]=="q":
                        stars+=int(answer[2])
                    elif answer[1]=="w":
                        starStreak+=int(answer[2])
                elif answerGuessedA==True:
                    print("\nYou've guess that word already, please guess another answer!")
                else:
                    lives-=1
                    if lives == 0:
                        makeGuy(0,score,hintUsed,hintsUsed,stars,starStreak)
                        score=0
                        print("\nhangman is no more, how could you! >:((\nRewinding...")
                        print("the word/phrase was "+word+" by the way.")
                    else:
                        print("\nThat was the wrong word, try again!")
                        guessedLetters.append(answer)
            elif answerGuessedA==True:
                print("\n You've already guessed that silly! Try again with something you haven't guessed yet!")
            else:
                for i in word:
                    if i == answer:
                        wrongA=False
                        if addedToGList==False:
                            guessedLetters.append(answer)
                            addedToGList=True
                            print("\nNice one, guess another, or if you've found all the letters or can make the word, guess it(inclde punctuation and especially quotations and ALL LOWERCASE)")
                if wrongA==True:
                    guessedLetters.append(answer)
                    lives-=1
                    if lives == 0:
                        makeGuy(0,score,hintUsed,hintsUsed,stars,starStreak)
                        score=0
                        print("\nhangman is no more, how could you! >:((\nRewinding...\nThe word was "+word+" by the way")
                        print("the word/phrase was "+word+" by the way.")
                    else:
                        print("\nThat letter is not in the answer, try again!")
        print(boxBottom)
    playrounds()
playrounds()
#add tictactoe minigame maybe, add lore bits and add the hints    




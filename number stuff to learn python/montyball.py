#import random and math
import math;
import random;
#test random number
randomx = random.randint(1,3);
print(randomx);

#wins and losses respectively because labubu tastes better than money
switchGoldLabubus = 0
switchOneHundredBucks = 0
goldLabubus = 0
oneHundredBucks= 0
#choices is the choices available, wrong choice is the one that is removed, goldLabubu is the target,
#and choice is the choice.
for i in range(1000000):
    choices=[1,2,3];
    wrongChoices=[1,2,3];
    wrongChoice = random.randint(1,3);
    goldLabubu = random.randint(1,3);
    choice = choices[random.randint(0,2)];
    #I miss my ternaries ;(
    if (wrongChoice == goldLabubu):
        del wrongChoices[wrongChoice-1];
        wrongChoice = wrongChoices[random.randint(0,1)];
    del choices[wrongChoice-1];
    newChoice = choices[random.randint(0,1)];
    if newChoice == choice:
        if newChoice == choices[0]:
            newChoice = choices[1];
        else:
            newChoice = choices[0];
    if (newChoice==goldLabubu):
        goldLabubus+=1;
    else:
        oneHundredBucks+=1;
#retrospectively, I was rlly lost in the sacue and I don't know why it returns 50/50s pls if someone actually reviews this tell me why
print(goldLabubus);
print(oneHundredBucks);
#gave up lol it kept giving 5050s





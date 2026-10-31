#collatz conjecture, lets see how my crusty chromebook handles this :confident cat:
#starts bu making a list to  put the numbers in and a list to count the steps it took for each
#the variable helps count the steps 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17];
steps = []



#run the rules: if it is odd, 3n+1, hence the name, and if it is even, n/2. i'll check the numbers in a 
#seperate code file.
for i in numbers:
    x=numbers[i-1];
    step=0;
    while (x!=1.0):
        if (x % 2 == 0):
            x = x/2;
            step+=1;
        else:
            x = (3 * x) + 1;
            step+=1;
    steps.append(step);
print(steps);    


#successful
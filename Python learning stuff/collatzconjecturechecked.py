#copypasted the code, this time, imma try and kill my computer. if the while never terminates, the conjecture is wrong.
#of course, the collatz conjecture is extremely famous and has been checked up to some grillions of numbers with supercomputers,
#so im not expecting discover anything with my chromebook, but still is fun to do

steps = [];

#adding numbers to list 
def collatz(ns):
    numbers = [];
    for i in range(ns):
        numbers.append(i);
#run the rules: if it is odd, 3n+1, hence the name, and if it is even, n/2. 
    for i in numbers:
        x=(numbers[i])+1;
        step=0;
        while (x!=1.0):
            if (x % 2 == 0):
                x = x/2;
            else:
                x = (3 * x) + 1;
            step+=1
        steps.append(step);
#print steps and the highest step count
    print(steps);
    p = max(steps);
    print("number that lasted most steps:")
    print(steps.index(p,0,len(steps)));
    print("lasted");
    print(p);
    print("steps");
collatz(10000000);
#of 10,000,000 numbers, 8400510 lasted the most, with 685 steps
#successful
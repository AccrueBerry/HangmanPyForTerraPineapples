#testing to see how the time for the calculations increases between magnitudes of 1.2
import math;
import time;

#list to keep track of those runtimes
times = [];

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
for i in range (10):
    runfor = round(1 * (1.2**i));
    startTime=time.perf_counter();
    collatz(runfor);
    doneTime=time.perf_counter();
    times.append(doneTime-startTime);
    print(times);
timeDifferencesadditive=[];
timeDifferencespercentage=[];
for i in range(len(times)):
    if i<len(times)-1:
        timeDifferencesadditive.append(times[i+1]-times[i]);
        timeDifferencespercentage.append(((times[i+1]/times[i])*100)-100);
print(timeDifferencesadditive);
print(timeDifferencespercentage);

#succesful
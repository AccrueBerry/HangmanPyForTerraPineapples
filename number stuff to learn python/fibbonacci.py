#list to start the sequence
x = [0,1];

# takes the last two digits, adds them with the plus sign, and appends them to the list using .append()
for i in range(15):
    x.append((x[i]+x[i+1]));

#prints the result
print(x);

#tried to use .input() but it wasnt working cuz I couldnt type into the output, which im asuuming is the 
#the console, but i coulsnt type into it and when it did let me tyoe into it I would not press enter to input.

#define the function with the code above
def fibonacci(p):
    x = [0,1];
    for i in range(p):
        x.append((x[i]+x[i+1]));
    print(x);

#this is where it all went wrong, it just doesnt like me bro
y = input("how many didgits of fibonacci do u want");
fibonacci(int(y));
#successful
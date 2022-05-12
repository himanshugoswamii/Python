
import random

x=random.randint(1,99)
for i in range(1,8,1):
    y=int(input("Enter a Number = "))
    
    if x>y:
        print("too low")
        if x-y<=5:
            print("you're too close")
    elif x<y:
        print("too high")
        if y-x<=5:
            print("you're too close")
            
    elif x==y:
        print("You guessed the correct number in the ",i, "th guess")
        break
    
else:
    print("You lost LOL,the secret number was ",x)            


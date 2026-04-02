import random as ra

counter = 0
counter_1 =10
number_guess = ra.randrange(1,100)
print("-----THE GUESSING GAME-----\n Choose a number between \n         1 and 100 ")
while counter != 10 :
    
    print(f"\nNumber of attempts left : {counter_1}")
    try:
        counter+=1
        entry_number = int(input(f"\nEnter a number : "))
        if number_guess == entry_number:
            print(f"\n         You Win \n Mukhtar number is : {number_guess} \n Number of attempts  : {counter} \n ")
            break
        elif number_guess < entry_number:
            print("\n Too low ")
        else:
           print("\n Too high ")

        counter_1-=1
    except:
        pass

print(f"\n        You lose \n Mukhtar number is : {number_guess} \n Number of attempts  : {counter}\n ")
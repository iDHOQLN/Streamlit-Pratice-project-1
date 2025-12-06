

##Number Guisinng game

import random

Secret_number = random.randint(1,50)
attempts = 0
 
print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

while True :
    try:
        Guess_number = int(input("Enter the GuessNumber "))
        attempts +=1


        if Guess_number < Secret_number :
            print("Number is lower ! Try Again ",Guess_number)
        elif Guess_number > Secret_number :
            print("Number is Higher ! Try Again",Guess_number)
        else:
            print(f"Congratulations! You guessed the number. {Secret_number} in {attempts} attempts")
            break

    except ValueError:
        print("Please Enter A valid Number" ,Guess_number)
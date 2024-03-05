import random

def numberGuessingGame ():
    while True:
        attempt=10
        number = random.randint(0,50)

        print("Guess a number between 0 and 50")
    
        while attempt>0:
            #to verify if the user entered a number
            input_user = input("Enter your guess :" )
            if input_user.isdigit():
                guess = int(input_user)
            else:
                print("Your guess has to be a number!")
                continue

            #the guess is correct
            if number == guess:
                print(f"You win! you guessed the correct number {number} in {10 - attempt + 1} attempts")
                break
            
            #the number is less than the guess
            if number < guess :
                print("your guess is too high. Try again!")

            #the number is more than the guess
            else:
                print("your guess is too low. Try again!")

            attempt -= 1
            print(f"You have {attempt} attempts left.")

        #no attempts left
        if attempt==0 :
            print(f"You lose! No more attempts left, the correct number is {number}")
            
        #to play again
        replay = input("play again? (y/n) : ")
        while replay not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            replay = input("Play again? (y/n): ")
        
        if replay == 'n':
            print("Goodbye!")
            return
            

#calling the function
numberGuessingGame ()
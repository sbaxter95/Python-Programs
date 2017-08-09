import random

def game():
    #Generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    max_guesses = 5

    while len(guesses) < max_guesses:
        try:
            #Get guess from player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            #Compare to actual number
            if guess == secret_num:
                print("Correct! My number was {}".format(secret_num))
                play_again()
                break
            elif guess > secret_num:
                print("Too high")
            else:
                print("Too low")
                    
            guesses.append(guess)
    else:
        print("You didn't get it. My number was {}".format(secret_num))
        play_again()

def play_again():
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        guesses = []
        game()
    else:
        print("Goodbye!")
        
game()

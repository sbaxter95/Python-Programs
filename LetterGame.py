import random
import os 
import sys

words=[
    'lemon',
    'lime',
    'melon',
    'apple',
    'banana',
    'strawberry',
    'berry',
    'pear'
]

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses,good_guesses, secret_word):
    clear()

    print ("Strikes {}/7".format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter)
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter)
        else:
            print('_')

    print('')

def get_guesses(bad_guesses,good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print ("You can just guess a letter at a time.")

        elif guess in bad_guesses or guess in good_guesses:
            print ("You already guessed that letter")

        elif  not  guess.isalpha():
            print( "You must always guess letters")
        else:
            return guess

def play(done):
    clear()
    secret_word= random.choice(words)
    bad_guesses=[]
    good_guesses=[]

    while True:
        draw(bad_guesses,good_guesses,secret_word)
        guess = get_guesses(bad_guesses,good_guesses)
        if guess in secret_word:
            good_guesses.append(guess)
            found=True
            for letter in secret_word:
                if letter not in good_guesses:
                    found=False
            if found:
                print('You win')
                print('The secret word was {}'.format(secret_word))
                done=True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses)==7:
                draw(bad_guesses,good_guesses,secret_word)
                print('You lost')
                print('The secret word was {}'.format(secret_word))
                done=True 

        if done:
            play_again=input('Wanna play again? Y/n').lower()
            if play_again!='n':
                return play(done=False)
            else:
                sys.exit()


done = False

while True:
    clear()
    play(done)

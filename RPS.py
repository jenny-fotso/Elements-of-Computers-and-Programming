# File: RPS.py
# Description: A program that allows a player to play the game Rock - Paper -
# Scissors against a computer opponent.
# Assignment Number: 7
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


# The purpose of this program is to practice creating expressions, using
# variables, conditional logic, loops, and user defined functions.
def main():
    name, rounds = intro()
    play_game(name, rounds)

def play_game(name, rounds):
    # Playing the game meaning running through all the functions.
    human_wins = 0
    for i in range (1, rounds + 1):
        print('**** Round', i, '****')
        human_choice = human_play(name)
        computer_choice, computer_word = computer_play()
        human_wins = compare(human_choice, computer_choice, human_wins)
    outro(rounds, human_wins, name)
    print('Well played.')

def get_input(prompt):
    # The input and thank you statements to reduce redundancy.
    print('***** INITIAL INPUT *****')
    result = input(prompt)
    print('Thank you!')
    print()
    return result

def intro():
    # All the intro print statements before the first round.
    print('Welcome to ROCK PAPER SCISSORS. I, Computer, will be your opponent.')
    name = get_input('Please enter your name: ')
    rounds = int(get_input('Please enter the number of rounds to play: '))
    set_the_seed = get_input('Please enter y if you want to set the seed: ').lower()
    if set_the_seed == 'y':
        print('***** INITIAL INPUT *****')
        num = int(input('Please enter an integer for the seed: '))
        print('Thank you!')
        random.seed(num)
    print()
    return name, rounds

def human_play(name):
    # Asking the user to play and assigning the input to a number to match that
    # of the computer's where 1 is rock, 2 is paper, and 3 is scissors.
    print(str(name) + ', enter your choice for this round.')
    human_choice = input('R for Rock, P for Paper, S for Scissors: ').upper()
    if human_choice == 'R':
        human_choice = 1
    elif human_choice == 'P':
        human_choice = 2
    else:
        human_choice = 3
    return human_choice

def computer_play():
    # Now the computer gets to play and we print the computer's choice.
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_word = 'Rock.'
    elif computer_choice == 2:
        computer_word = 'Paper.'
    else:
        computer_word = 'Scissors.'
    print('I pick', computer_word)
    return computer_choice, computer_word

def compare(human_choice, computer_choice, human_wins):
    # Comparing the user and the computer's choice to determine the winner and
    # adding up the user's wins.
    if human_choice == 3 and computer_choice == 1:
        print('Rock breaks Scissors. I win.')
    elif human_choice == 1 and computer_choice == 3:
        print('Rock breaks Scissors. You win.')
        human_wins += 1
    # walk thru each case
    elif (human_choice < computer_choice) and human_choice == 2:
        print('Scissors cut Paper. I win.')
    elif (human_choice < computer_choice) and human_choice == 1:
        print('Paper covers Rock. I win.')
    elif human_choice > computer_choice and human_choice == 2:
        print('Paper covers Rock. You win.')
        human_wins += 1
    elif human_choice > computer_choice and human_choice == 3:
        print('Scissors cut Paper. You win.')
        human_wins += 1
    else:
        print('We picked the same thing. Round is a draw.')
    print()
    return human_wins
    
def outro(rounds, human_wins, name):
    # A summary of some of the statistics of the game.
    if rounds == 0:
        print('We played 0 rounds of ROCK PAPER SCISSORS.')
        print(name, 'won 0 rounds.')
    elif rounds == 1:
        print('We played 1 round of ROCK PAPER SCISSORS.')
    else:
        print('We played', rounds, 'rounds of ROCK PAPER SCISSORS.')
    if human_wins == 1:
        print(name, 'won 1 round.')
    else:
        print(name, 'won', human_wins, 'rounds.')
            

main()

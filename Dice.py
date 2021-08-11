# File: Dice.py
# Description: A program that plays a simplified version of craps and prints
# out various statistics about the simulation.
# Assignment Number: 6
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


# The purpose of this program is to practice using variables, creating
# expressions, conditional logic, and loops.
def main():
    # Ask the user if they want to set the initial seed and how many rounds
    # they would like to simulate.
    print('This program simulates the dice game of craps.')
    question = input('Do you want to set the seed? Enter y for yes,'
                     + ' anything else for no: ')
    if question  == 'y':
        num = int(input('Enter an int for the initial seed: '))
        random.seed(num)
    total_rounds = int(input('Enter the number of rounds to run: '))

    # Create variables for the statistics of the simulation that are going
    # to be outputted at the end of the program.
    start_round = 0
    wins = 0
    if total_rounds <= 0:
        current_rolls = 0
        total_rounds = 0
    else:
        current_rolls = 1

    # Simulate the given number of rounds.
    while start_round < total_rounds:
        initial_roll = random.randint(1, 6) + random.randint(1, 6)
        round_rolls = 1
        winning = (initial_roll == 7 or initial_roll == 11)
        losing = (initial_roll == 2 or initial_roll == 3 or initial_roll == 12)
        if winning:
            wins += 1
        if not winning and not losing:
            point = initial_roll
            value = random.randint(1, 6) + random.randint(1, 6)
            round_rolls += 1
            while value != 7 and value != point:
                value = random.randint(1, 6) + random.randint(1, 6)
                round_rolls += 1
            if value == point:
                wins +=1
        if round_rolls > current_rolls:
            current_rolls = round_rolls
        start_round += 1

    # Print out how many times the player wins and the maximum number of rolls
    # in any given round.                    
    print('Player won ' + str(wins) + ' times in ' + str(total_rounds)
          + ' rounds.')
    print('Maximum number of rolls in a round = ' + str(current_rolls))
                    

main()

# 1. For most inputs in the simulation, especially as the number of rounds
# gets larger, the player ends up winning a little less than half of the
# rounds played. The probability of winning or losing isn't
# large enough for the game to favor either the player or the casino (the
# odds are almost 50/50), so I do not think the simulation supports the idea
# that casinos end up winning in the long run. 

# 2. I'm keeping the money. Like I said earlier, the odds are almsot 50/50
# so essentially, even if I played, I would still lose roughly a little more
# than a $1,000 and win a little less than $1,000 which would leave me with
# a little less than $2,000. I know a probabilty is just a measurement and
# the result of the actual game might end up different, but 500 rounds is a
# signifcant number so the wins and losses are more likely to converge to that
# probability because of the magnitude of experiments, so no I would not
# play craps, I'd just keep the money instead. If it was like 3 or 4 rounds then
# yeah i'd bet some money, but I guess there's not really any fun in that :/


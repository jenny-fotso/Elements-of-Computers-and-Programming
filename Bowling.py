# File: Bowling.py
# Description: A program that calculates a bowler's average and handicap
# based on three inputted game scores.
# Assignment Number: 3
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
# Slip days used this assignment: 0
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.


# Using strings and variables, and creating expressions to return the
# average and handicap values of the user's games.
def main():
    # Asking the user to input all necessary information.
    name = input('Enter your name: ')
    print()
    game_one = eval(input('Enter Game 1: '))
    game_two = eval(input('Enter Game 2: '))
    game_three = eval(input('Enter Game 3: '))
    print()

    # Calculating the average and the handicap.
    average = int((game_one + game_two + game_three) / 3)
    handicap = (200 - average) * 0.8
    
    # Printing the average and handicap values to the user.
    print(name + '\'s average is: ' + str(average))
    print(name + '\'s handicap is: ' + str(int(handicap)))
    print()


main()
    


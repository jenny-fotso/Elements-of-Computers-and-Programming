# File: Zeller.py
# Description: A program that prompts the user to enter a date
# (day, month, year) and prints out the day of the week for that date.
# Assignment Number: 5
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny Fotso, this programming assignment is my own work
# and I have not provided this code to any other student.


# Creating expressions, using variables and conditional logic to return
# the day of the week given the inputted date.
def main():
    # Asking the user to input all necessary information.
    month = input('Enter the month (for example, January, February, etc.): ')
    day_in_month = int(input('Enter the day (an integer): '))
    year = int(input('Enter the year (an integer): '))

    # Assigning integers to each month according to the algorithm.
    if month == 'March':
        month_number = 3
    elif month == 'April':
        month_number = 4
    elif month == 'May':
        month_number = 5
    elif month == 'June':
        month_number = 6
    elif month == 'July':
        month_number = 7
    elif month == 'August':
        month_number = 8
    elif month == 'September':
        month_number = 9
    elif month == 'October':
        month_number = 10
    elif month == 'November':
        month_number = 11
    elif month == 'December':
        month_number = 12
    elif month == 'January':
        month_number = 13
        year -= 1
    elif month == 'February':
        month_number = 14
        year -= 1
        
    # Calculations using Zeller's congruence.
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = (year // 4) + (year // 400)
    century_days = year // 100
    total_days = (day_in_month + variation_in_days_per_month + year
        + leap_year_days - century_days)
    day_of_week = total_days % 7

    day_word = ''

    # Formatting the output.
    if day_of_week == 0:
        day_word = 'Saturday'
    elif day_of_week == 1:
        day_word = 'Sunday'
    elif day_of_week == 2:
        day_word = 'Monday'
    elif day_of_week == 3:
        day_word = 'Tuesday'
    elif day_of_week == 4:
        day_word = 'Wednesday'
    elif day_of_week == 5:
        day_word = 'Thursday'
    else:
        day_word = 'Friday'

    print('The day of the week is' + str(day_word) + '.')


main()

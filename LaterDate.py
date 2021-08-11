# File: LaterDate.py
# Description: A program that prompts the user to enter a year, month,
# day and the number of days to skip, then determines the date after
# the number of days to skip.
# Assignment Number: 4
#
# Name: Jenny Fotso
# EID:  
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.


# The purpose of this program is to practice using variables, creating
# expressions, and using conditional logic.
def main():
    # Ask the user to input all the day.
    print('This program asks for a date and days to skip.')
    print('It then displays the date that many days after the given date.')
    print()
    month = str(input('Enter the month: '))
    day = int(input('Enter the day of the month: '))
    year = int(input('Enter the year: '))
    print()
    skip = int(input('Enter the number of days to skip: '))

    #Programming the stuff.
    new_day = day + skip
    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if new_day > 31 and month == 'January':
        new_month = 'February'
        new_day -= 31
    elif new_day > 29 and month == 'February' and leap_year:
        new_month = 'March'
        new_day -= 29
    elif new_day > 28 and month == 'February' and not leap_year:
        new_month = 'March'
        new_day -= 28
    elif new_day > 31 and month == 'March':
        new_month = 'April' 
        new_day -= 31
    elif new_day > 30 and month == 'April':
        new_month = 'May'
        new_day -= 30
    elif new_day > 31 and month == 'May':
        new_month = 'June'
        new_day -= 31
    elif new_day > 30 and month == 'June':
        new_month = 'July'
        new_day -= 30
    elif new_day > 31 and month == 'July':
        new_month = 'August'
        new_day -= 31
    elif new_day > 31 and month == 'August':
        new_month = 'September'
        new_day -= 31
    elif new_day > 30 and month == 'September':
        new_month = 'October'
        new_day -= 30
    elif new_day > 31 and month == 'October':
        new_month = 'November'
        new_day -= 31
    elif new_day > 30 and month == 'November':
        new_month = 'December'
        new_day -= 30
    elif new_day > 31 and month == 'December':
        new_month = 'January'
        new_day -= 31
        year += 1
    else:
        new_month = month
        
    #Printing the output.
    if skip > 1:
        print(skip, ' days after ', month, ' ', day, ', ', year, ' is ',
              new_month, ' ', new_day, ', ', year,'.', sep='')
    else:
        print('1 day after ', month, ' ', day, ', ', year, ' is ',
              new_month, ' ', new_day, ', ', year,'.', sep='')
    print()


main()











        

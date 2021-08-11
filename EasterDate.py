# File: EasterDate.py
# Description: A program to calculate the month and day of the Easter
# holiday for any given year using a provided formula.
# Assignment Number: 2
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny Fotso, this programming assignment is my own work
# and I have not provided this code to any other student.


# Using variables and creating expressions to return the month and day
# of Easter given the inputted year.
def main():
    # Ask the user for the year and save the year in a variable.
    year = eval(input('Enter year: '))
    
    # Calculate the date of Easter using the Computus algorithm.
    lunar_year_cycle_position = year % 9
    weekday_slide_part_1 = year % 4
    weekday_slide_part_2 = year % 7
    leap_year_100 = year // 100
    leap_year_400 = leap_year_100 // 4
    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25
    century_start = (15 - lunar_orbit_correction
                     + leap_year_100 - leap_year_400) % 30
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7
    days_added = (19 * lunar_year_cycle_position + century_start) % 30
    day_of_week_offset = (2 * weekday_slide_part_1
                          + 4 * weekday_slide_part_2
                          + 6 * days_added + sunday_offset) % 7
    total_days_added = 22 + days_added + day_of_week_offset
    day_of_easter = total_days_added % 31
    month_of_easter = 3 + (total_days_added // 31)
    
    # Print the result.
    print('In', year, 'Easter Sunday is on month', month_of_easter,
           'and day', day_of_easter)
    

main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

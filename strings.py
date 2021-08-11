# File: strings.py
# Description: A program that implements three different, unrelated functions
# revolving around manipulating the inputted strings.
# Assignment Number: 9
#
# Name: Jenny Fotso
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler Vestal
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.

# The purpose of this program is to practice creating functions that manipulate
# and use strings.


# This function returns the number of characterss in s1 and s2 that match based
# on position.
def num_chars_same(s1, s2):
    length = min(len(s1),len(s2))
    count = 0
    for i in range(length):
        if s1[i] == s2[i]:
            count += 1
    return count


# The function returns a stretched version of s1 with each character repeated.
# The number of repitions is num times the position of that character if we
# were to use 1 based indexing. 
def stretch(s1, num):
    string = ''
    for i in range(1, len(s1) + 1):
        rep = s1[i-1] * num * i
        string += rep
    return string


# The function returns the number of characters at the end of s1 and s2 that
# match. Stops at the first mistmatched character.
def length_of_matching_suffix(s1, s2):
    length = min(len(s1),len(s2))
    count = 0
    for i in range(1, length + 1):
        if s1[-i] == s2[-i]:
            count += 1
        else:
            return count
    return count


# Run tests on the functions. Ask the user for input.
def main():
    num_tests = eval(input('Enter the number of tests per method: '))
    print('Testing num chars same function.')
    test_functions_with_two_string_parameters(num_tests, num_chars_same)
    print('Testing stretch function.')
    stretch_tests(num_tests)
    print('Testing length of matching suffix function.')
    test_functions_with_two_string_parameters(num_tests,
                                              length_of_matching_suffix)


# Test the functions that take 2 String parameters.
def test_functions_with_two_string_parameters(num_tests, function_to_test):
    for i in range(0, num_tests):
        s1 = input('Enter first string: ')
        s2 = input('Enter second string: ')
        print(function_to_test(s1, s2))
    print()


# Test the stretch function.
def stretch_tests(num_tests):
    for i in range(0, num_tests):
        s1 = input('Enter the string: ')
        num = eval(input('Enter number of times to repeat: '))
        print(stretch(s1, num))
    print()
    
            
main()

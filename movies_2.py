# File: movies_2.py
# Description: A program uses dictionaries to find what words
# appear in reviews with good and bad ratings,
# as well as the length of good and bad reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 13
#
# Name: Jenny Fotso
# EID:  
# Email: fortsojenny@utexas.edu
# Grader: Skyler
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.


# Read the main data file and run the menu loop.
def main():
    print('Welcome to the movie sentiment program - Version 2.')
    file_name = input('Enter file name with reviews: ')
    words_dictionary, num_words_dictionary = get_dictionaries(file_name)
    choice = get_choice()
    while '1' <= choice <= '3':
        # Get the index of the function to call.
        if choice == '1':
            show_individual_stats(words_dictionary, 'a word')
        elif choice == '2':
            cutoff_stats(words_dictionary)
        else:
            show_individual_stats(num_words_dictionary, 'the number of words')
        choice = get_choice()

    
# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See statistics for a given word.')
    print('2. See all words that meet given cut-offs.')
    print('3. See statistics for reviews with a given number of words.')
    print('4. Or anything else to quit.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create and return two dictionaries.
# All strings in reviews are shifted to lower case.
#
# The first dictionary has keys that are words (any and all
# strings in the reviews) with the value a list of length 2.
# Both elements of the list are integers.
# The first element in the list is the number of reviews that
# contain the word (key) and the second is the sum of all the
# review scores that contain the word (key). 
# 
# The second dictionary has keys that are also strings representing
# the number of words (any and all strings) in a review.
# So for example '12' if the review has 12 words. The value
# for each key is also a list of length 2.Just like the first
# dictionary the first element in the list is the number of reviews
# that contain the word (key) and the second is the sum of all the
# review scores that contain the word (key).
def get_dictionaries(file_name):
    infile = open(file_name)
    words = {}
    num_words = {}
    # Process each line in the file.
    for line in infile:
        line = line.lower()
        words_in_file = line.split()
        for word in words_in_file[1:]:
            # If we've seen this key (word) before, we increase the values
            if word in words:
                index = words[word]
                index[0] += 1
                index[1] += int(line[0])
            # If not, then we add it to the 1st dictionary
            else:
                words[word] = [1, int(line[0])]
        # If we've seen this key (line length) before, we increase the values
        if str(len(words_in_file) - 1) in num_words:
            index = num_words[str(len(words_in_file) - 1)]
            index[0] += 1
            index[1] += int(line[0])
        # If not, then we add it to the 2nd dictionary
        else:
            num_words[str(len(words_in_file) - 1)] = [1, int(line[0])]
    infile.close()
    return words, num_words


# Ask the user for a key and print the statistics for that key,
# if present in the given dictionary.
def show_individual_stats(dictionary, prompt):
    search = input('Enter ' + prompt + ': ')
    if search.lower() in dictionary:
        total = dictionary[search.lower()][1]
        reviews =  dictionary[search.lower()][0]
        print('Number of reviews =', reviews)
        average = total / reviews
        print('Average review score =', average)
    else:
        print(search, 'is not present in the dictionary.')
        

# Ask the user if they want words above or below a given cutoff.
# Get the cutoff for average review score and the minimum number of reviews
# the word must appear in and print the results.
def cutoff_stats(words_dictionary):
    choice = input('Enter the letter a to show scores above a given cutoff,\n' +
                   'anything else to show scores below a given cutoff: ')
    cutoff = eval(input('Enter the score cutoff between 0 and 4: '))
    number = eval(input('Enter the minimum number of reviews required: '))
    print('Results: ')
    for key in words_dictionary:
        reviews = words_dictionary[key][0]
        total  = words_dictionary[key][1]
        average = total / reviews
        if ((choice == 'a' and average >= cutoff and reviews >= number)
        or (choice == 'b' and average <= cutoff and reviews >= number)):
            print('word = ' + key + '. Number of reviews = ' + str(reviews)
                  + '. Average review score = ' + str(average))

                
main()


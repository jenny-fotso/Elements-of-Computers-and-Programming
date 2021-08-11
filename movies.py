# File: movies.py
# Description: A program works with movie ratings and reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 12
#
# Name: Jenny Fotso 
# EID: 
# Email: fotsojenny@utexas.edu
# Grader: Skyler
#
# On my honor, Jenny, this programming assignment is my own work
# and I have not provided this code to any other student.


# Read the main data file and run the menu loop.
def main():
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    choice = get_choice()
    # List of our functions. They all take a single parameter, the reviews.
    functions = [print_word_sentiment, print_sentiments_from_file,
                 print_longest_review, print_shortest_review]
    VALUE_1 = ord('1')
    while '1' <= choice <= '4':
        # Get the index of the function to call.
        index = ord(choice) - VALUE_1
        function = functions[index](reviews)            
        choice = get_choice()

    
# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See average rating for a word.')
    print('2. Show average reviews for all words in a file.')
    print('3. See the longest review.')
    print('4. See the shortest review.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create a list of lists with the movie reviews.
# All letters in the reviews are converted to lower case.
def get_reviews(file_name):
    infile = open(file_name)
    lines = infile.readlines()
    list_of_lists = []
    for line in lines:
        line_list = (line.lower()).split()
        line_list[0] = int(line_list[0])
        list_of_lists.append(line_list)
    infile.close()
    return list_of_lists
    

# Get a word from the user and determine the average rating of
# reviews that contain that word. 
def print_word_sentiment(reviews):
    search = str(input('Enter the word to search for: '))
    count = 0
    total = 0
    for i in range(len(reviews)):
        if search.lower() in reviews[i]:
            count += 1
            total += int(reviews[i][0])
    if count == 0:
        print(search, 'did not appear in any reviews')
    elif count == 1:
        average = float(total / count)
        print(search, 'appeared in', count,
              'review. Average review score =', average)
    else:
        average = float(total / count)
        print(search, 'appeared in', count,
              'reviews. Average review score =', average)


# Ask the user for the name of a file with words and phrases.
# For each word in the file, determine and show
# the average rating of reviews that contain the given word.
def print_sentiments_from_file(reviews):
    file_name = input('Enter file name with words to check: ')
    infile = open(file_name)
    lines = infile.readlines()
    for i in range(len(lines)):
        count = 0
        total = 0
        search = lines[i].strip()
        for j in range(len(reviews)):
            if search.lower() in reviews[j]:
                count += 1
                total += int(reviews[j][0])
        print('Word number ', i + 1, ' is ', '\'', search, '\'. Results: ', sep = '')
        if count == 0:
            print(search, 'did not appear in any reviews')
        elif count == 1:
            average = float(total / count)
            print(search, 'appeared in', count,
                  'review. Average review score =', average)
        else:
            average = float(total / count)
            print(search, 'appeared in', count,
                  'reviews. Average review score =', average)
        print()
        

# Print information about the longest review.
def print_longest_review(reviews):
    longest = -1
    for i in range(len(reviews)):
        if len(reviews[i]) > longest:
            longest = len(reviews[i]) - 1
            element = i
        elif len(reviews[i]) == longest:
            longest = len(reviews[element]) - 1
    print('Longest review has', longest, 'words.')
    print('Review as list:', reviews[element][1:])
    

# Print information about the shortest review.
def print_shortest_review(reviews):
    shortest = len(reviews[0])
    for i in range(1, len(reviews)):
        if len(reviews[i]) < shortest:
            shortest = len(reviews[i]) - 1
            element = i
        elif len(reviews[i]) == shortest:
            shortest = len(reviews[element]) - 1
    print('Shortest review has', shortest, 'words.')
    print('Review as list:', reviews[element][1:])
    

main()


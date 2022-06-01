
# Define a function named is_two. It should accept one input and return 
# True if the passed input is either the number or the string 2, 
# False otherwise.
from re import T


def is_two(n):
    n == "two" or n== '2'

# Define a function named is_vowel. It should return True if the 
# passed string is a vowel, False otherwise.
def is_vowel(string):
    return len(string) == 1 and string.lower() in 'aeiou'

# Define a function named is_consonant. It should return True if 
# the passed string is a consonant, False otherwise. Use your is_vowel 
# function to accomplish this.
def is_consonant(string):
    return len(string) == 1 and not is_vowel(string) and string.isalpha()


# Define a function that accepts a string that is a word. The function 
# should capitalize the first letter of the word if the word starts with a 
# consonant.

def capitalize_starting_consonant(string):
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
        return string


# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to 
# tip.
def caclulate_tip(tip_percentage, bill):
amount_to_tip = bill * tip_percentage

# Define a function named apply_discount. It should accept a original 
# price, and a discount percentage, and return the price after the 
# discount is applied.

# Define a function named handle_commas. It should accept a string that 
# is a number that contains commas in it as input, and return a number as 
# output.

# Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

# Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed.

# Define a function named normalize_name. It should accept a string and 
# return a valid python identifier, that is:

# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# Additional Exercise

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
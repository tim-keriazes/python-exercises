
# Define a function named is_two. It should accept one input and return 
# True if the passed input is either the number or the string 2, 
# False otherwise.

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
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to 
# tip.

def calculate_tip(tip_percentage, bill):

    amount_to_tip = bill * tip_percentage
    return amount_to_tip



# Define a function named apply_discount. It should accept a original 
# price, and a discount percentage, and return the price after the 
# discount is applied.

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount

#apply_discount(45, .5)
#22.5

# Define a function named handle_commas. It should accept a string that 
# is a number that contains commas in it as input, and return a number as 
# output.

def handle_commas(number_string):
    string_without_commas = number_string.replace(',','')
    actual_number = int(string_without_commas)
    return actual_number
#handle_commas('1,293,239,239,244')
#1293239239244
#could check and confirm with type(handle_commas('1,293,239,239,244'))

# Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >=90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    else:
        return " Grade must be a number"
    
# get_letter_grade(69)
# 'D'

# Define a function named remove_vowels that accepts a string and 
# returns a string with all the vowels removed.

def is_vowel(string):
    return len(string) == 1 and string.lower() in 'aeiou'
def is_consonant(string):
    return len(string) == 1 and not is_vowel(string) and string.isalpha()
def remove_vowels(string):
    output = ''
    for char in string:
        if is_consonant(char):
            output += char
    return output

# Define a function named normalize_name. It should accept a string and 
# return a valid python identifier, that has no whitespace, lowercase, valid identifier:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])


def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return special_char_removed.lower().strip().replace(' ', '_')

# normalize_name('s,uper funny norma,l')
#'super_funny_normal'


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(nums):
    output = []
    total = 0
    for num in nums:
        total += num
        output.append(total)
    return output
#cumulative_sum([1,2,3])
#[1, 3, 6]

# Additional Exercise

# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

import imported_func 


# Exercises
# You will need to use imports to complete each exercise; in addition, these exercise will strengthen your problem solving and python coding skills.
# You will be directed to create specific files in part 1, for the rest you may do your work in either import_exercises.py or import_exercises.ipynb.
# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

imported_func.is_vowel('a')
#true
imported_func.is_vowel('k')
#false
imported_func.is_vowel('apple')
#false




# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

imported_func.calculate_tip(.2, 100)
#20
imported_func.calculate_tip(.45, 1843)
#829.35

# Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.

import imported_func as f
f.get_letter_grade(65)
#'D'

# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

# Read about and use the itertools module from the python standard library to help you solve the following problems:

import itertools

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
list(itertools.product("abc", [1, 2, 3]))

# [('a', 1),
#  ('a', 2),
#  ('a', 3),
#  ('b', 1),
#  ('b', 2),
#  ('b', 3),
#  ('c', 1),
#  ('c', 2),
#  ('c', 3)]
# can combine nine different ways

# How many different combinations are there of 2 letters from "abcd"?
len(list(itertools.combinations('abcd',2)))
#6 combinations

# How many different permutations are there of 2 letters from "abcd"?
len(list(itertools.permutations('abcd',2)))
#12 permutations

# Save this file as profiles.json inside of your exercises directory (right click -> save file as...).

# Use the load function from the json module to open this file.


# import json

# json.load(open('profiles.json'))
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users

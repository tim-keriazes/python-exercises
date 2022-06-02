
# Conditional Basics

# prompt the user for a day of the week, print out whether the day is 
# Monday or not

day = input('Please enter the day of the week: ')
if day.lower() in ['monday', 'mon']:
    print('Today is Monday')
else:
    print (f'Today is {day.capitalize()}')

# prompt the user for a day of the week, print out whether the day is a 
# weekday or a weekend

day = input('Please enter the day of the week: ')
#make sure input is valid
while day.lower() not in ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']:
    print ('Input not valid. Please enter the name of the day')
    day = input('Please enter the day of the week: ')
#is input weekday or weekend
if day.lower()in['saturday','sunday']:
    print('Today is a weekend')
else:
    print('Today is a weekday')

# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 50
hourly_rate = 55
overtime_rate = hourly_rate * 1.5
# variables and values

if hours_worked <= 40:
    total_pay = hours_worked  * overtime_rate
else:
    regular_pay = hourly_rate * 40
    overtime_pay = ( hours_worked - 40 ) * overtime_rate
    total_pay = regular_pay + overtime_pay
total_pay

# Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:

i = 5
while i<= 15:
    print(i)
    i = i + 1 #increment value of i by one


# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.


i = 0
while i <= 100:
    print(i)
    i = i +2 #count by 2s


# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    i = i -5 #count back by 5 from 100 to -10


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
#Output should equal:
#  2
#  4
#  16
#  256
#  65536

i = 2
while i < 1000000:
    print(i)
    i *= i

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i = i - 5
    
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5


# For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

num = input ('Please enter a positive integer')
num = int(num)
for i in range (1,11):
    print(F' {num} * {i} = {num * i }')


# Create a for loop that uses print to create the output shown below.
for i in range(1,10):
    print(str(i)*i)

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
#continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this).
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# Your output should look like this:
# Number to skip is: 27
# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

num = input ('Please Enter an Odd Number Between 1 and 50: ')
#we want to make sure input is correct
# isdigit= False
# > 50
# <=0
# num % 2 == 0

while True:
    if (num.isdigit() == False
        or int(num) > 50
        or int(num)< 1
        or int(num) % 2 == 0
       ):
        print('Invalid Input')
        num = input('Please Enter an Odd Number Between 1 and 50: ')
    else:
        break
#convert input string to integer
num = int(num)

#print odd numbers and skip chosen
print('The Number to Skip is ', num)
for i in range (1,50):
    if i% 2 == 0:
        continue
    elif i == num:
        print('Skipping this Number', i)
    else:
        print('Here is an Odd Number', i)



# The input function can be used to prompt for input and use that input in your python code. 
#Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, also note that the input 
#function returns a string, so you'll need to convert this to a numeric type.)

num = input('Please input a positive integer: ')
while True:
    if (num.isdigit() ==  False
        or int(num) < 0):
            print('Invalid Input')
            num = input('Please input a positive integer: ')
    else:
        break
        #checks if the input is valid

for i in range (0, int(num) +1):
    print(i)
        
# Write a program that prompts the user for a positive integer. Next write a loop that prints out the 
#numbers from the number the user entered down to 1.

num = input('Please input a positive integer: ')
while True:
    if (num.isdigit() ==  False
        or int(num) < 0):
            print('Invalid Input')
            num = input('Please input a positive integer: ')
    else:
        break
        #checks if the input is valid

for i in reversed (range (1, int(num) +1)):  #reversed function of the range, same as before, instead of ending at 0, end at 1
    print(i)


# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
#Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range (1, 101):
    if(i % 3 == 0) and (i % 5 == 0):  #divisible by both 3 and 5 then print
        print('FizzBuzz')
    elif i % 3 == 0:                  #elif divisible by 3 then print 
        print('Fizz')
    elif i % 5 == 0 :                 #elif divisible by 5 then print
        print('Buzz')
    else:
        print(i)


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

num = input('Please Enter a Positive Integer: ')

print('Here is the table')
print('number|squared|cubed')
print('------|------|------')

num = int(num)
for i in range (1, num +1):
    
    #print(f'{i} |{i ** 2} |{i ** 3}')
      print(f'{i:^6}|{i ** 2:^6}|{i ** 3:^6}')
        
# Please Enter a Positive Integer: 6
#Here is the table
#number|squared|cubed
#------|------|------
#  1   |  1   |  1   
#  2   |  4   |  8   
#  3   |  9   |  27  
#  4   |  16  |  64  
#  5   |  25  | 125  
#  6   |  36  | 216        
        
        
# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

while True:
    num = input('Please enter a numerical grade: ')
    num = int(num)
    if num in range(88, 101):
        print('A')
    elif num in range(80, 88):
        print('B')
    elif num in range(67, 80):
        print('C')
    elif num in range(60, 67):
        print('D')
    else:
        print('F')
    choice = input('Do you want to continue: ')
    if choice.lower() in ['yes','y']:
        continue
    else:
        break
# Please enter a numerical grade: 100
# A
# Do you want to continue: y
# Please enter a numerical grade: 88
# A
# Do you want to continue: y
# Please enter a numerical grade: 80
# B
        
        
# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. Loop through the 
# list and print out information about each book.

books = [
    {
        'title':'title1',
        'author': 'author1',
        'genre': 'genre1'
    },
    {
        'title':'title2',
        'author': 'author1',
        'genre': 'genre2'
    },
    {
        'title':'title3',
        'author': 'author2',
        'genre': 'genre2'
    },
    {
        'title':'title4',
        'author': 'author3',
        'genre': 'genre2'
    }
]

#
#
[book for book in books]

# [{'title': 'title1', 'author': 'author1', 'genre': 'genre1'},
#  {'title': 'title2', 'author': 'author1', 'genre': 'genre2'},
#  {'title': 'title3', 'author': 'author2', 'genre': 'genre2'},
#  {'title': 'title4', 'author': 'author3', 'genre': 'genre2'}]

# for book in books:
#    print(f"The book {book['title']} by {book['author']} belongs to genre {book['genre']}")


# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

user_input = input('Please enter a genre: ')
l = []
for book in books:
    if book['genre'] == user_input:
        l.append(book['title']
print(l)
if len(l) == 0:
    print('No matching title found')
    print('Please choose from genre1, genre2')

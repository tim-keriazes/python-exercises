from operator import truediv
from re import X

from scipy.misc import face


type(99.9)
#float
type("false")
# string
type(False)
# bool
type('0')
#string
type(0)
#integer
type(true)
#bool
type('True')
#string
type([{}])
#list
type({'a':[]})
#dict


# A term or phrase typed into a search box?
#string
# If a user is logged in?
#bool
# A discount amount to apply to a user's shopping cart?
#float
# Whether or not a coupon code is valid?
#bool
# An email address typed into a registration form?
#string
# The price of a product?
#float
# A Matrix?
#dict
# The email addresses collected from a registration form?
#list
# Information about applicants to Codeup's data science program?
#string

# '1' + 2
# error

# 6 % 4
#2

# type(6 % 4)
#int

# type(type(6 % 4))
#type

# '3 + 4 is ' + 3 + 4
#error

# 0 < 0
#false

# 'False' == False
#false

# True == 'True'
#false

# 5 >= -5
#true

# True or "42"
#true

# 6 % 5
#1

# 5 < 4 and 1 == 1
#false

# 'codeup' == 'codeup' and 'codeup' == 'Codeup'
#false

# 4 >= 0 and 1 !== '1'
#error

# 6 % 3 == 0
#true

# 5 % 2 != 0
#true

# [1] + 2
#error

# [1] + [2]
#[1,2]

# [1] * 2
#[1,1]

# [1] * [2]
#error

# [] + [] == []
#true

# {} + {}
#error

# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't 
# know yet if they're going to like it). If price for a movie per day is 3 
# dollars, how much will you have to pay?

rented_movies=X #define variable
x={"littlemermaid":3,"brotherbear":5,"hercules":1} #variable is a dict
price = sum(x.values())*3 # sum elements in dict
print(price) #print (27)

# Suppose you're working as a contractor for 3 companies: Google, Amazon 
# and Facebook, they pay you a different rate per hour. Google pays 400 
# dollars per hour, Amazon 380, and Facebook 350. How much will you receive 
# in payment for this week? You worked 10 hours for Facebook, 6 hours for 
# Google and 4 hours for Amazon.
#6530

google_hourly = 400
amazon_hourly = 380
facebook_hourly = 350

#define hourly rates

google_pay = 6 * google_hourly
amazon_pay = 4 * amazon_hourly
facebook_pay = 10 * facebook_hourly

#reference rates and input hours

total_pay = google_pay + amazon_pay + facebook_pay

#sum the pays to get total pay, print

print(total_pay)







# A student can be enrolled to a class only if the class is not 
# full and the class schedule does not conflict with her current schedule.
#true

class_has_room= True
Schedule_works= True
can_be_enrolled = class_has_room and Schedule_works
print(can_be_enrolled)



# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.
#
more_than_two = False
offer_still_good = True
premium_member = True
#define arguments which will be used in the logic statement

offer_can_be_applied = offer_still_good and (more_than_two or premium_member)
offer_can_be_applied
#True
#
#
#
username = 'codeup'
password = 'notastrongpassword'

#create variable that holds the boolean for each of the following
#at least five characters
#username must be less than 20 characters
#password must not be the same as the username
#bonus neither can start or end with whitespace

#five characters
at_least_five_characters = len(password)> 5
at_least_five_characters

#username less than 20
username_less_than_20 = len(username) < 20
username_less_than_20

#password different from username
password_not_the_username = username != password

#remove the whitespaces
username_no_whitespace=username ==username.strip()
password_no_whitespace=password ==password.strip()

#put it together
good_username = username_less_than_20 and username_no_whitespace
good_password = at_least_five_characters and password_not_the_username and password_no_whitespace

#if these are both true then the combination is good

good_combination = good_username and good_password
good_combination
#true
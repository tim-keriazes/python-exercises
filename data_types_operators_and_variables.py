from re import X


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
price = sum(x.values()) # sum elements in dict
print(price) #print

# Suppose you're working as a contractor for 3 companies: Google, Amazon 
# and Facebook, they pay you a different rate per hour. Google pays 400 
# dollars per hour, Amazon 380, and Facebook 350. How much will you receive 
# in payment for this week? You worked 10 hours for Facebook, 6 hours for 
# Google and 4 hours for Amazon.
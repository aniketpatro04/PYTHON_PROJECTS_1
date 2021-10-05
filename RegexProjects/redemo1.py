# importing the regular expression module
import re

# Creating a regular expression object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# if the pattern is found, it will return a match object. We are storing the returned value in an arbitrary variable.
mo = phoneNumRegex.search('My number is 415-555-4242')

# Printing the exact text using the .group() function.
print('Phone number found : ' + mo.group())

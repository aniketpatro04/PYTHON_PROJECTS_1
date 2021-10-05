# Importing the requests library
import requests

r = requests.get('https://xkcd.com/353/')  # Sending the request to the desired URL.

print(r)  # If the request was successful you would get 200 as the output of this stmt.

# print(dir(r))  # A quick trick to list all the attributes and methods of any object.

# For a more detailed explanation pass it through the help function. Ex help(r).

# print(r.text)  # To get the content of the response in unicode. This will most probably will give you an html output
# of the url. You can use a html parser to parse this info.

# Let's try to download an image using the requests library.

r1 = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r1.content)  # This gives the output in bytes.

# Let's try to put that image in a particular file to be viewed.

# with open('comic.png', 'wb') as f:  # Here 'wb' means opening it in write byte mode since our output will be in bytes.
#     f.write(r.content)

# Let's check weather we get a good response or not

print(r.status_code)
print(r.ok)  # Returns true for anything less than a 400s error.


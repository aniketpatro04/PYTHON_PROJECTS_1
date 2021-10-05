import requests

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/', params=payload)

print(r.url)

# Posting data to a route.

data1 = {'username': 'dude', 'password': 'testing'}
r1 = requests.post('https://httpbin.org/post', data=data1)

print(r1.json())  # A better way to handle json responses. This will create a python dictionary.

# Performing logins through authentications.

# Using Basic authentication.

r2 = requests.get('https://httpbin.org/basic-auth/dude/testing', auth=('dude', 'testing'))
print(r2.text)

# The requests library is designed to wait indefinitely until its gets a response from the website. In such a case we
# can use a timeout with any request with the help of an additional parameter.

r3 = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r3)

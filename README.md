# gimme-py

A Python library for the Gimme private API

### Example API usage

	>>> from pprint import pprint
	>>> from gimme import GimmeRequest
	
	# Follow a user
	>>> req = GimmeRequest(auth_token, cmd=set_favorite_celebrity_insert, celebrityCode='Soobin')
	>>> pprint(req)


### Example convience functions usage

	>>> from pprint import pprint
	>>> from gimme import Gimme

	>>> g = Gimme(auth_token)
	
	# Request a users timeline
	>>> feed = g.timeline(username='Kaeun')
	>>> pprint(feed)

	# Iterate over a timeline
	>>> for feed in g.itimeline():
	>>>     pprint(feed)

### Obtaining the authToken

	>>> from gimme import GimmeAuth
	
	>>> auth = GimmeAuth('username', 'password')
	>>> print(auth.authToken)
	
	# Write the auth token to a file for later use
	>>> auth.write('my_gimme_authToken.json')
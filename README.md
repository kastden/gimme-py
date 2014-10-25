# gimme-py

A Python library for the Gimme private API

### Example API usage

	>>> from pprint import pprint
	>>> from gimme import GimmeRequest
	
	# Follow a user
	>>> req = GimmeRequest(auth_token, cmd='set_favorite_celebrity_insert', celebrityCode='Soobin')
	>>> pprint(req)


### Example convenience methods usage

	>>> from pprint import pprint
	>>> from gimme import Gimme

	>>> g = Gimme(auth_token)
	
	# Request a user's timeline
	>>> feed = g.timeline(username='Kaeun')
	>>> pprint(feed)

	# Iterate over a timeline
	# itimeline accepts the same arguments as the timeline method
	>>> for message in g.itimeline():
	>>>     pprint(message)

### Obtaining the authToken

	>>> from gimme import GimmeAuth
	
	>>> auth = GimmeAuth('username', 'password')
	>>> print(auth.authToken)
	
	# Write the auth token to a file for later use
	>>> auth.write('my_gimme_authToken.json')
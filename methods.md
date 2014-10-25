
# Gimme private API methods 

### Timelines:  

##### Common for both methods:

	# There are five different message types:
	# 0 is all messages
	# 1 is voice only
	# 2 is photos only
	# 3 is messages for all fans
	# 4 is replies
	type = '0'

	# createdAt is a timestamp in the format of "2014-09-27 22:28:11"
	# It is optional, but can be used for traversing an timeline
	createdAt = 'date time'

##### Various timelines:

	# Retrieve a celebrities timeline:
	cmd = 'get_celebrity_message_list_for_fan'
	code = username
#
	# Retrieve the home timeline:
	cmd = 'get_celebrity_timeline_list'

### Follow/unfollow users
	# Follow a user:
	cmd = 'set_favorite_celebrity_insert'
	celebrityCode = username
#	
	# Unfollow a user:
	cmd = 'set_favorite_celebrity_delete'
	celebrityCode = username
#
	# Get following list
	cmd = 'get_favorite_celebrity_list'

### User information/editing
	# Get a list of all the celebrities on Gimme with their user information
	cmd = 'get_celebrity_list'
#
	# Retrieve information about the currently logged in user:
	cmd = 'get_my_profile'
#
	#Change user information for the currently logged in user:
	cmd = 'set_user_profile_modify'
	# Nickname, max 12 characters
	nickname = 'ilovegown'
	# Gender is M for male and F for female
	gender = 'M"
	# Country is a two character ISO country code
	country = 'fr'
	# Introduce is a text describing yourself
	introduce = 'I like memes, thanks'
	# Birth is your birthday in the format of YYYY.MM.DD
	birth = '1975.04.13'
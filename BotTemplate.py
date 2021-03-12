"""
TWITTERBOT-BUILDING TEMPLATE:
Phillip Brooker

The following code provides the building blocks on which you can build a fully-
functioning Twitter bot. The code below imports tweepy (a Twitter API library
which allows Python to speak to Twitter), imports various application
credentials (i.e. "passwords" that allow you to log in to one of your Twitter
accounts), and then posts a pre-specified message to that account's timeline.

The trick now is to use the stuff here to build your own Twitter Bot with
extended functions and capabilities - do you want your Twitter bot to respond
to specific phrases posted by other users? Do you want it to produce something
more randomised and varied than a single pre-specified piece of text? Do you
want your bot to be able to store and re-use information that people post to it?
All these things (and way more) are very much possible, but you'll need to get
into the tweepy/Twitter and Python documentation to explore how to do so. Have
fun!
"""

#You will need to install the "tweepy" library before running the code. Give
#Phil a shout and he can help you.
import tweepy

#This code is for importing relevant "log-in details" from a separate file
#called AppCred. To put together your own AppCred file, follow the instructions
#given in the TECHNICAL5/TwitterBot folder. This is how you set up a Twitter
#account to be used as a bot (for various reasons it's more straightforward to
#do this from an account you already use rather than set up a fresh one).
from AppCred import CONSUMER_KEY, CONSUMER_SECRET
from AppCred import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#This is the code that establishes what the bot actually does. And this is the
#bit you should play around with. Note the activity we're asking the bot to do
#is incredibly mundane and simple; when you run the code it will just post a
#rather boring message. Can you build some code that makes your bot do something
#more exciting and more relevant to the purposes of social science research?
api.update_status("Bot-test: success!")

"""
OTHER USEFUL BOT-ISH COMMANDS YOU MAY WANT TO DRAW ON:

#Send a direct message to a specified user
api.send_direct_message(USERNAME_OR_USERID, "Message text")

#Follow and unfollow other specified users
api.create_friendship(USERNAME_OR_USERID)
api.destroy_friendship(USERNAME_OR_USERID)

#Like/favourite another tweet (with tweet ID number)
api.create_favorite(ID)

#Block and remove blocks of other specified users
api.create_block(USERNAME_OR_USERID)
api.destroy_block(USERNAME_OR_USERID)
"""

import mysql.connector
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

from own_info import twitter 
from tweet_table import table as tb
from tweet_listener import listener

def main():
	print('Twitter Streaming!')
	print('-'*50)
	conn = mysql.connector.connect(user='root',
                                	password='',
                                	host='localhost')
	table=tb(conn)
	# Create the database
	table.create_db('tweet')
	# Use that database
	table.use_db('tweet')
	# Clean the database
	table.clean_db()
	# Show the tables
	table.show_tables()
	# Create the table
	table.create_table('text(time INT(13), username VARCHAR(20), tweet VARCHAR(140))')
	# Show the tables
	table.show_tables()

	# Set up the twitter app info
	t = twitter()
	auth = OAuthHandler(t.ckey, t.csecret)
	auth.set_access_token(t.atoken, t.asecret)

	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=['car'], languages=['en'], stall_warnings=True)

if __name__ == '__main__':
	main()

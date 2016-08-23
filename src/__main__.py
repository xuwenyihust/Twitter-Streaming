import mysql.connector
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

from own_info import twitter 
from tweet_op import database as db
from tweet_op import table as tb

def main():
	print('>>> Twitter Streaming!')
	print('-'*50)
	conn = mysql.connector.connect(user='root',
                                	password='',
                                	host='localhost')
	c = conn.cursor()

	database = db(conn)

	# Create the database
	database.create('tweet')
	# Use that database
	database.use('tweet')
	# Clean the database
	database.clean()
	# Show the tables
	database.show_tables()

	# Create the tables
	table_text = tb(conn, 'text')
	database.create_table('text' + '(time INT(13), username VARCHAR(20), tweet VARCHAR(140) CHARACTER SET utf8mb4)')
	# Show the tables
	database.show_tables()
	# Describe the table
	table_text.describe()

	# Setup the keywords
	keywords = ['car', 'fish', 'nba', 'overwatch']
	table_source = tb(conn, 'source')
	database.create_table('source' + '(id INT(13), keyword VARCHAR(20))')
	table_source.build_source( keywords)
	table_source.describe()	

	# Set up the twitter app info
	t = twitter()
	auth = OAuthHandler(t.ckey, t.csecret)
	auth.set_access_token(t.atoken, t.asecret)

	# Modify the StreamListener class
	class listener(StreamListener):

		def __init__(self):
			self.counter = 0
			self.limit = 5

		def on_data(self, data):
			all_data = json.loads(data)
			# Check to unsure there's text in the json data		
			if 'text' in all_data:
				if self.counter < self.limit:
					self.counter += 1
					tweet = all_data['text']
					username = all_data['user']['screen_name']

					c.execute('INSERT INTO text (time, username, tweet) VALUES (%s, %s, %s)', (time.time(), username, tweet))
					conn.commit()

					#print((username, tweet))
				else:
					#print('-'*50)
					return False
			return True
		
		def on_error(self, status):
			print(status)

	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=['i'], languages=['en'])

	# Check the table
	table_source.head(5)
	table_text.head(5)

	# Close the connection
	conn.close()
	print('>>> Connection closed!')

if __name__ == '__main__':
	main()

import mysql.connector
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

from own_info import twitter 
from tweet_table import table as tb

def main():
	print('>>> Twitter Streaming!')
	print('-'*50)
	conn = mysql.connector.connect(user='root',
                                	password='',
                                	host='localhost')
	c = conn.cursor()

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
	table_name = 'text'
	table.create_table(table_name + '(time INT(13), username VARCHAR(20), tweet VARCHAR(140) CHARACTER SET utf8mb4)')
	# Show the tables
	table.show_tables()
	# Describe the table
	table.describe_table(table_name)

	# Set up the twitter app info
	t = twitter()
	auth = OAuthHandler(t.ckey, t.csecret)
	auth.set_access_token(t.atoken, t.asecret)

	# Modify the StreamListener class
	class listener(StreamListener):

		def __init__(self):
			self.counter = 0
			self.limit = 20

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
	table.head(10, table_name)

	# Close the connection
	conn.close()
	print('>>> Connection closed!')

if __name__ == '__main__':
	main()

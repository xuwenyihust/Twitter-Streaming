import mysql.connector
import time

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

from own_info import twitter
from tweet_listener import listener 
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

	# Setup the keywords
	keywords = ['car', 'fish', 'nba', 'overwatch']
	table_source = tb(conn, 'source')
	table_text = []
	database.create_table('source' + '(id INT(13), keyword VARCHAR(20))')
	table_source.build_source( keywords)
	table_source.describe()	

	# Set up the twitter app info
	t = twitter()
	auth = OAuthHandler(t.ckey, t.csecret)
	auth.set_access_token(t.atoken, t.asecret)

	tracks = table_source.extract_source()	
	for x in tracks:
		database.create_table(x + '(time INT(13), username VARCHAR(20), tweet VARCHAR(140) CHARACTER SET utf8mb4)')
		table_text.append(tb(conn, x))
		twitterStream = Stream(auth, listener(x))
		twitterStream.filter(track=[x], languages=['en'])
		time.sleep(5)

	# Check the table
	'''database.show_tables()
	table_source.head(5)
	for x in table_text:
		x.head(5)'''

	# Close the connection
	conn.close()
	print('>>> Connection closed!')

if __name__ == '__main__':
	main()

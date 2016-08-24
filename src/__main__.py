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
	database.create('Twitter')
	# Use that database
	database.use('Twitter')
	# Clean the database
	database.clean()
	# Show the tables
	database.show_tables()

	# Setup the keywords in table source
	keywords = ['blizzard', 'tokyo', 'nba']
	table_source = tb(conn, 'source')

	database.create_table('source', 'source' + '(id INT(13), keyword VARCHAR(20))')
	table_source.build_source( keywords)
	table_source.describe()	

	# Set up the twitter app info
	t = twitter()
	auth = OAuthHandler(t.ckey, t.csecret)
	auth.set_access_token(t.atoken, t.asecret)
	
	# Extract the keywords stored in table source
	# For each keyword create a table
	tracks = table_source.extract_source()	
	for x in tracks:
		database.create_table('tweet_'+x, 'tweet_'+x +'(id VARCHAR(140), time INT(13), username VARCHAR(20), tweet VARCHAR(140) CHARACTER SET utf8mb4)')		
		database.create_table('hashtag_'+x, 'hashtag_'+x+'(id VARCHAR(140), tag VARCHAR(140) CHARACTER SET utf8mb4)')
		database.create_table('url_'+x, 'url_'+x+'(id VARCHAR(140), url VARCHAR(140))')
		database.create_table('mention_'+x, 'mention_'+x+'(id VARCHAR(140), mentioned_id VARCHAR(140), mentioned_name VARCHAR(140))')		

		twitterStream = Stream(auth, listener(x))
		twitterStream.filter(track=[x], languages=['en'])
		time.sleep(3)
	
	#twitterStream = Stream(auth, listener('car'))
	#twitterStream.filter(track=['car'], languages=['en'])

	# Have streamed tweets into txt files now

	# Check the table
	database.show_tables()

	# Close the connection
	conn.close()
	print('>>> Connection closed!')

if __name__ == '__main__':
	main()

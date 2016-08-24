import mysql.connector
from tweepy.streaming import StreamListener
import json
import time

# Modify the StreamListener class
class listener(StreamListener):

	def __init__(self, term):
		self.counter = 0
		self.limit = 10
		self.term = term
		#self.output = open('data/text_'+term+'.txt', 'w')
		self.conn = mysql.connector.connect(user='root',
                                    password='',
                                    host='localhost')
		self.c = self.conn.cursor()
		self.c.execute('USE Twitter')
	

	def on_data(self, data):
		# Read each tweet into a dictionary
		tweetdict = json.loads(data)

		if self.counter < self.limit:
			# Increment the counter
			self.counter += 1
			# Extract diff fields from the tweet dictionary
			tweet = tweetdict['text']
			username = tweetdict['user']['screen_name']
			id = tweetdict['id_str']
			hashdict = tweetdict['entities']['hashtags']
			urldict = tweetdict['entities']['urls']
			userdict = tweetdict['entities']['user_mentions']

			self.c.execute('INSERT INTO tweet_'+self.term+' (id, time, username, tweet) VALUES (%s, %s, %s, %s)', (id, time.time(), username, tweet))
			self.conn.commit()

			# Access each hashtag mentioned in a tweet
			for x in hashdict:
				tag = x['text']
				self.c.execute('INSERT INTO hashtag_'+self.term+' (id, tag) VALUES (%s, %s)', (id, tag))
				self.conn.commit()

			# Access each url mentioned in a tweet
			for x in urldict:
				url = x['url']
				self.c.execute('INSERT INTO url_'+self.term+' (id, url) VALUES (%s, %s)', (id, url))
				self.conn.commit()	

			# Access each user mentioned in a tweet
			for x in userdict:
				mentioned_id = x['id']
				mentioned_name = x['name']
				self.c.execute('INSERT INTO mention_'+self.term+' (id, mentioned_id, mentioned_name) VALUES (%s, %s, %s)', (id, mentioned_id, mentioned_name))
				self.conn.commit()	

			return True
		else:
			self.conn.close()
			return False

	def on_error(self, status):
		print(status)


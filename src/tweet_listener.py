from tweepy.streaming import StreamListener
import json

# Modify the StreamListener class
class listener(StreamListener):

	def __init__(self, term):
		self.counter = 0
		self.limit = 5
		self.term = term
		self.output = open('data/text_'+term+'.txt', 'w')

	def on_data(self, data):
		all_data = json.loads(data)
		# Check to unsure there's text in the json data     
		if 'text' in all_data:
			if self.counter < self.limit:
				self.counter += 1
				tweet = all_data['text']
				username = all_data['user']['screen_name']

				#c.execute('INSERT INTO ' + self.table_name  +  ' (time, username, tweet) VALUES (%s, %s, %s)', (time.time(), username, tweet))
				#conn.commit()
				self.output.write(str(username)+'|||'+str(tweet)+'\n')

			else:
				return False
		return True

	def on_error(self, status):
		print(status)

